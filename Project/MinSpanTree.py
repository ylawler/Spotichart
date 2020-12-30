import networkx as nx
from networkx.algorithms import tree
import matplotlib.pyplot as plt

class MinSpanTree:

    def __init__(self):
        self.MST_graph = nx.Graph()

    def create_min_span_tree(self, edge_dict):
        G = nx.Graph()
        for edge in edge_dict:
            G.add_edge(edge[0], edge[1], weight=edge_dict[edge])
        mst = tree.minimum_spanning_tree(G, weight = 'weight', algorithm='kruskal')
        self.MST_graph = mst


#if __name__ == '__main__':
    # edge_list = {('a', 'b'): 5,
    #              ('b', 'c'): 7,
    #              ('c', 'd'): 4,
    #              ('d', 'e'): 1,
    #              ('a', 'd'): 10
    #              }
    # mst = MinSpanTree()
    # mst.create_min_span_tree(edge_list)
    # print(mst.MST_graph)

