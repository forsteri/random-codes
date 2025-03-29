from PIL import Image
import os

input_folder = "input_images"
output_folder = "resized_images"
# 出力フォルダが存在しない場合は作成
os.makedirs(output_folder, exist_ok=True)

# 入力フォルダ内の画像ファイルを1つずつ処理
for filename in os.listdir(input_folder):
    # 拡張子が.jpgまたは.pngのファイルのみ処理
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # 画像ファイルを開いて300px × 300pxにリサイズ
        with Image.open(os.path.join(input_folder, filename)) as img:
            # リサイズ
            resized = img.resize((300, 300))  # 幅300px × 高さ300px
            # リサイズした画像を保存
            resized.save(os.path.join(output_folder, filename))
