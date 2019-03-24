from pathlib import Path
import re
import json
from tqdm import tqdm as tqdm
from gensim.models.phrases import Phrases , Phraser
from collections import Counter
from itertools import chain
import pandas as pd
import pickle

def doc_from_allfiles():
# テキストファイルのディレクトリ、テキストファイル名を指定
    filepath = Path('/home/suzuki/notebooks/xmlparse/aip2018/textfiles')
    files1 = list(filepath.glob('*.txt'))
#     jsonfile = Path(filepath, 'offset.json')
#     with jsonfile.open() as fj:
#         offset1 = json.load(fj)

    filepath2 = Path('/home/suzuki/notebooks/xmlparse/aps2018/textfiles')
    files2 = list(filepath2.glob('*.txt'))
#     jsonfile = Path(filepath2, 'offset.json')
#     with jsonfile.open() as fj:
#         offset2 = json.load(fj)

    filepath3 = Path('/home/suzuki/notebooks/xmlparse/jap2005/textfiles')
    files3 = list(filepath3.glob('*.txt'))
#     jsonfile = Path(filepath3, 'offset.json')
#     with jsonfile.open() as fj:
#         offset3 = json.load(fj)

    filepath4 = Path('/home/suzuki/notebooks/xmlparse/iop2018/textfiles')
    files4 = list(filepath4.glob('*.txt'))
#     jsonfile = Path(filepath4, 'offset.json')
#     with jsonfile.open() as fj:
#         offset4 = json.load(fj)        

    files_all = files1 + files2 + files3 + files4

    # df = pd.concat([df_aip2018, df_jap2005, df_aps2018, df_iop2018])
    # offset = offset1
    # offset.update(offset2)
    # offset.update(offset3)
    # offset.update(offset4)

    docs = []
    for file in tqdm(files_all[:]):
        with open(file) as f:
            doc = f.read()
        docs.append(doc)

    return docs