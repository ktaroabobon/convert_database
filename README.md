# Converter Database

## はじめに  
このパッケージは、csv, excel, sql(MYSQL, SQLite3)のどれか一方からもう一方に変更するものです。（例：csv形式->sqlite3形式）

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

③最後にpythonを用いて実行してください。
```
python main.py
```

## 注意点
- 対応しているファイルの拡張子は以下の通りです。  
csvファイル：csv  
excelファイル：xlsx 
sqlite3ファイル：db, sqlite3
  
- csvファイルの場合はsetting.ini/table_nameはnoneで構いません。
