import duckdb
import pandas as pd

# DuckDBに接続（メモリ内データベース）
con = duckdb.connect(database=':memory:')

# テーブル作成と簡単なデータの挿入
con.execute("""
CREATE TABLE stocks (
    date DATE,
    symbol VARCHAR,
    price DECIMAL(10, 2),
    volume INTEGER
)
""")

# データを挿入
con.execute("""
INSERT INTO stocks VALUES
    ('2023-01-01', 'AAPL', 150.75, 1000000),
    ('2023-01-01', 'MSFT', 250.30, 800000),
    ('2023-01-01', 'GOOGL', 120.50, 600000),
    ('2023-01-02', 'AAPL', 152.00, 1200000),
    ('2023-01-02', 'MSFT', 248.50, 750000),
    ('2023-01-02', 'GOOGL', 122.75, 650000),
    ('2023-01-03', 'AAPL', 153.25, 1300000),
    ('2023-01-03', 'MSFT', 251.00, 900000),
    ('2023-01-03', 'GOOGL', 123.00, 700000)
""")

# クエリを実行して結果を表示
print("===== 全データの表示 =====")
result = con.execute("SELECT * FROM stocks").fetchall()
for row in result:
    print(row)

print("\n===== 日付ごとの平均価格 =====")
avg_prices = con.execute("""
    SELECT date, AVG(price) as avg_price
    FROM stocks
    GROUP BY date
    ORDER BY date
""").fetchall()
for row in avg_prices:
    print(f"日付: {row[0]}, 平均価格: {row[1]:.2f}円")

print("\n===== 銘柄ごとの価格変動 =====")
price_changes = con.execute("""
    SELECT 
        symbol, 
        FIRST(price) as first_price,
        LAST(price) as last_price,
        (LAST(price) - FIRST(price)) / FIRST(price) * 100 as price_change_pct
    FROM stocks
    GROUP BY symbol
    ORDER BY price_change_pct DESC
""").fetchall()
for row in price_changes:
    print(f"銘柄: {row[0]}, 初日価格: {row[1]}円, 最終日価格: {row[2]}円, 変動率: {row[3]:.2f}%")

# Pandas連携の例
print("\n===== Pandasとの連携 =====")
# DuckDBのクエリ結果をPandas DataFrameに変換
df = con.execute("SELECT * FROM stocks").df()
print(df.head())

# DataFrameからDuckDBでクエリ
print("\n===== DataFrameに対するDuckDBクエリ =====")
result_df = duckdb.query("SELECT symbol, AVG(price) as avg_price FROM df GROUP BY symbol").df()
print(result_df)

# 接続を閉じる
con.close()