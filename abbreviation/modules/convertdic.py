import Levenshtein
import itertools
import networkx as nx
import community

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
    #                 abbs = re.sub(r' \(.+?\)', '', abbs)
                    rev_abbrev.append([k, abbs])
            else:
                abb = ''.join(v).replace('_', ' ')
    #             abb = re.sub(r' \(.+?\)', '', abb)
                rev_abbrev.append([k, abb])
    return rev_abbrev