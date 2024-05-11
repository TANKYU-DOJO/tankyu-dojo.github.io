from jinja2 import Template, Environment, FileSystemLoader
import os
from glob import glob

# カレントディレクトリをJinjaに読み込ませる
env = Environment(loader=FileSystemLoader(os.getcwd(), encoding='utf8'))

# 拡張子 .jinja のファイルを再帰的に探索
for file in glob('**/*.jinja', recursive=True):
    # アンダーバーから始まるテンプレートファイルは無視する
    if not file.startswith('_'):
        # テンプレートファイルを読み込む
        template = env.get_template(file)
        # 出力するファイルを開く
        output = open(os.path.splitext(file)[0] + '.html', 'w')
        # 書き出す
        output.write(template.render())
        output.close()