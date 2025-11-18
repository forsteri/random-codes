import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

class SalesDataGenerator:
    """販売データ生成クラス - データ量をパラメータで指定可能"""
    
    def __init__(self, 
                 num_customers=1000,
                 num_products=100,
                 num_orders=5000,
                 start_date='2023-01-01',
                 end_date='2024-12-31'):
        """
        Parameters:
        -----------
        num_customers : int
            顧客数
        num_products : int
            商品数
        num_orders : int
            注文数（注文明細はこの1.5〜3倍程度になる）
        start_date : str
            データ生成開始日
        end_date : str
            データ生成終了日
        """
        self.num_customers = num_customers
        self.num_products = num_products
        self.num_orders = num_orders
        self.start_date = pd.to_datetime(start_date)
        self.end_date = pd.to_datetime(end_date)
        
        # シード設定（再現性のため）
        np.random.seed(42)
        random.seed(42)
    
    def generate_customers(self):
        """顧客マスタ生成"""
        prefectures = ['東京都', '大阪府', '神奈川県', '愛知県', '福岡県', 
                      '北海道', '埼玉県', '千葉県', '兵庫県', '京都府']
        customer_segments = ['プレミアム', 'スタンダード', 'ライト']
        
        customers = pd.DataFrame({
            'customer_id': [f'C{str(i).zfill(8)}' for i in range(1, self.num_customers + 1)],
            'customer_name': [f'顧客{i}' for i in range(1, self.num_customers + 1)],
            'email': [f'customer{i}@example.com' for i in range(1, self.num_customers + 1)],
            'prefecture': np.random.choice(prefectures, self.num_customers),
            'age': np.random.randint(18, 75, self.num_customers),
            'gender': np.random.choice(['男性', '女性', 'その他'], self.num_customers),
            'customer_segment': np.random.choice(customer_segments, self.num_customers, 
                                                p=[0.1, 0.5, 0.4]),
            'registration_date': pd.date_range(
                start=self.start_date - timedelta(days=365),
                end=self.start_date,
                periods=self.num_customers
            )
        })
        
        return customers
    
    def generate_products(self):
        """商品マスタ生成"""
        categories = ['電化製品', '衣料品', '食品', '書籍', '家具', 
                     'スポーツ用品', '美容・健康', 'おもちゃ']
        
        products = pd.DataFrame({
            'product_id': [f'P{str(i).zfill(6)}' for i in range(1, self.num_products + 1)],
            'product_name': [f'商品{i}' for i in range(1, self.num_products + 1)],
            'category': np.random.choice(categories, self.num_products),
            'unit_price': np.random.randint(500, 50000, self.num_products),
            'cost_price': None,  # 後で計算
            'stock_quantity': np.random.randint(0, 1000, self.num_products),
            'supplier_id': [f'S{str(i).zfill(4)}' for i in np.random.randint(1, 51, self.num_products)]
        })
        
        # 原価は販売価格の50〜70%
        products['cost_price'] = (products['unit_price'] * 
                                 np.random.uniform(0.5, 0.7, self.num_products)).astype(int)
        
        return products
    
    def generate_orders(self, customers):
        """注文ヘッダ生成"""
        payment_methods = ['クレジットカード', '代引き', '銀行振込', 'コンビニ払い']
        order_statuses = ['完了', '配送中', 'キャンセル', '返品']
        
        # 日付をランダムに生成
        date_range = (self.end_date - self.start_date).days
        random_days = np.random.randint(0, date_range + 1, self.num_orders)
        order_dates = [self.start_date + timedelta(days=int(d)) for d in random_days]
        
        orders = pd.DataFrame({
            'order_id': [f'O{str(i).zfill(10)}' for i in range(1, self.num_orders + 1)],
            'customer_id': np.random.choice(customers['customer_id'], self.num_orders),
            'order_date': order_dates,
            'payment_method': np.random.choice(payment_methods, self.num_orders),
            'order_status': np.random.choice(order_statuses, self.num_orders, 
                                           p=[0.85, 0.08, 0.05, 0.02]),
            'shipping_fee': np.random.choice([0, 500, 800], self.num_orders, 
                                           p=[0.3, 0.5, 0.2]),
            'total_amount': 0  # 後で計算
        })
        
        return orders.sort_values('order_date').reset_index(drop=True)
    
    def generate_order_items(self, orders, products):
        """注文明細生成"""
        order_items = []
        
        for _, order in orders.iterrows():
            # 1注文あたり1〜5商品
            num_items = np.random.randint(1, 6)
            selected_products = products.sample(num_items)
            
            for _, product in selected_products.iterrows():
                quantity = np.random.randint(1, 4)
                discount_rate = np.random.choice([0, 0.05, 0.1, 0.2], p=[0.7, 0.15, 0.1, 0.05])
                
                order_items.append({
                    'order_id': order['order_id'],
                    'product_id': product['product_id'],
                    'quantity': quantity,
                    'unit_price': product['unit_price'],
                    'discount_rate': discount_rate,
                    'subtotal': int(product['unit_price'] * quantity * (1 - discount_rate))
                })
        
        order_items_df = pd.DataFrame(order_items)
        
        # 注文ヘッダの合計金額を更新
        order_totals = order_items_df.groupby('order_id')['subtotal'].sum()
        orders['total_amount'] = orders['order_id'].map(order_totals) + orders['shipping_fee']
        
        return order_items_df, orders
    
    def generate_all(self):
        """全データ生成"""
        print(f"データ生成開始...")
        print(f"  顧客数: {self.num_customers:,}")
        print(f"  商品数: {self.num_products:,}")
        print(f"  注文数: {self.num_orders:,}")
        
        customers = self.generate_customers()
        print(f"✓ 顧客データ生成完了")
        
        products = self.generate_products()
        print(f"✓ 商品データ生成完了")
        
        orders = self.generate_orders(customers)
        print(f"✓ 注文データ生成完了")
        
        order_items, orders = self.generate_order_items(orders, products)
        print(f"✓ 注文明細データ生成完了（{len(order_items):,}件）")
        
        return {
            'customers': customers,
            'products': products,
            'orders': orders,
            'order_items': order_items
        }
    
    def save_to_csv(self, data_dict, output_dir='data'):
        """CSVファイルに保存"""
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        for table_name, df in data_dict.items():
            file_path = f"{output_dir}/{table_name}.csv"
            df.to_csv(file_path, index=False, encoding='utf-8-sig')
            print(f"✓ {file_path} に保存しました（{len(df):,}件）")


# ===== 使用例 =====

# パターン1: 極小サイズ（開発・テスト用）
print("=" * 50)
print("【極小サイズ】")
print("=" * 50)
generator_tiny = SalesDataGenerator(
    num_customers=100,
    num_products=50,
    num_orders=500
)
data_tiny = generator_tiny.generate_all()
generator_tiny.save_to_csv(data_tiny, output_dir='data/tiny')
