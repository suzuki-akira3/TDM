import Levenshtein
import itertools
import networkx as nx
import community
import re

def std_Lev(s1, s2):
    return Levenshtein.distance(s1, s2)/(max(len(s1), len(s2)) * 1.00)

def acronim_dic(dic):
    rev_abbrev = []
    for k, v in dic.items():
    #     print(k)
        if len(v)>0:
            if len(v) >1:
                edges = ()
                G = nx.Graph()
                G.add_nodes_from(v)
                comb = list(itertools.combinations(v,2))
                weight = []
                for i in range(len(comb)):
                    ld = Levenshtein.distance(*comb[i])
                    sl = std_Lev(*comb[i])
#                     if ld < 6 :
                    if sl < 0.25:
                        weight.append((*comb[i], 1))
                G.add_weighted_edges_from(weight)

                partition = community.best_partition(G)
                for i in set(partition.values()):
                    abbs = '; '.join([kk for kk, vv in partition.items() if vv==i]).replace('_', ' ')
                    abbs = re.sub(r' \(.+?\)', '', abbs)
                    rev_abbrev.append([k, abbs])
            else:
                abb = ''.join(v).replace('_', ' ')
                abb = re.sub(r' \(.+?\)', '', abb)
                rev_abbrev.append([k, abb])
    return rev_abbrev

def concat_dic(dica, dicb):
    keysa = dica.keys()
    keysb = dicb.keys()
    new_keys = sorted(set(list(keysa) + list(keysb)))
    new_dic = {}
    for k in new_keys:
        new_values = []
        if dica.get(k):
            new_values.extend(dica[k])         
        if dicb.get(k): 
            new_values.extend(dicb[k])       
            
        new_dic[k] = list(sorted(set(new_values)))
        
    return new_dic
# m_dic = concat_dic(acronyms_dic['abb1'], acronyms_dic['abb2'])


## 接頭語の確認 1番目の単語のみ 余分な前後の単語を削除
def acr_check(phrase):
    acr = re.search(r'\(([A-Z\-–]+)s?\)', phrase).group(1) # 接頭語グループ用
    phrase2 = re.sub(r'\)[_\- \/][\w\-_ ]+$', ')', phrase) # class 2用 ()の後ろを削除 # スペース追加
    wl = re.split('_|-', phrase2.replace('-', '#-'))

    new_phrase = ''
    for i in range(len(wl)):
        if wl[0][0:1].lower() == acr[0:1].lower():   
            if re.match(''.join([r'[\w#]+'+c for c in acr[1:].replace('-', '')]), '_'.join(wl[:-1]), re.I): # 間に接頭語の2文字目以降が存在する場合
                new_phrase = '_'.join(wl).replace('#_', '-')
            break
        else:
            del wl[0] # 先頭単語が接頭語の最初の文字でなかった場合削除
    return new_phrase