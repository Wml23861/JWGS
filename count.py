import os
import re
import glob

files = sorted(glob.glob(r'e:\经文故事\金刚经\正文\第*品*.md'))
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    # 去除markdown标记
    content = re.sub(r'^#+\s*', '', content, flags=re.MULTILINE)
    content = re.sub(r'`', '', content)
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    # 移除空白
    content = re.sub(r'\s', '', content)
    # 只统计中文字符
    chinese = re.findall(r'[\u4e00-\u9fff]', content)
    total = len(content)
    name = os.path.basename(f)
    print(f'{name}: Chinese={len(chinese)}, Total={total}')
