import os

# 現在のディレクトリ内のファイルのリストを取得
files = os.listdir()

# 各ファイルに対して処理を実行
for filename in files:
    # ファイル名にスペースが含まれているか確認
    if " " in filename:
        # スペースをアンダーバーに置換
        new_filename = filename.replace(" ", "_")
        # ファイル名を変更
        os.rename(filename, new_filename)
        print(f"{filename} を {new_filename} に変更しました")

print("ファイル名が正常に更新されました。")
