from pathlib import Path
import pandas as pd
import json
import re
import shutil
from tqdm import tqdm as tqdm

# テキストファイルのディレクトリ、テキストファイル名を指定
filepath = Path('/home/suzuki/notebooks/xmlparse/aip2018/textfiles')
files1 = list(filepath.glob('*.txt'))