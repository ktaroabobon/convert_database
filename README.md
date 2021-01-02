# Converter Database

## はじめに  
このパッケージは、csv, excel, sql(MYSQL, SQLite3)のどれか一方からもう一方に変更するものです。（例：csv形式->sqlite3）

## Get Started  
①まずは必要なモジュールをダウンロードしましょう。  
```angular2html
pip install -r requirements.txt
```

②次に、import_dataフォルダーに変換対象のデータを入れてください。また、setting.iniの内容を適当な値に直してください。
```setting.ini
[import]
type = csv
file_name = test_csv
table_name = none

[output]
type = sqlite3
file_name = test_sqlite3
table_name = test_table
```
*なお、csvの場合はtable_name = noneで問題ありません。

③最後にpythonを用いて実行してください。
```
python main.py
```