from pathlib import Path
import json
import re

txtpath = Path('./aip2018/textfiles')
txtfiles = txtpath.glob('*.txt')

for txtfile in txtfiles:
    with txtfile.open(encoding='utf-8') as f:
        doc = f.read()

    print(doc)
