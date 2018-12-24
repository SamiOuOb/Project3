import numpy as np
import networkx as nx
import math
import matplotlib.pyplot as plt
from pygraph.classes.digraph import digraph
import time

class HITSIterator:
    __doc__ 

    def __init__(self, dg):
        self.max_iterations = 100  # 最大疊代數
        self.min_delta = 0.0001  
        self.graph = dg

        self.hub = {}
        self.authority = {}
        for node in self.graph.nodes():
            self.hub[node] = 1
            self.authority[node] = 1

    def hits(self):
        if not self.graph:
            return

        flag = False
        for i in range(self.max_iterations):
            change = 0.0  # 紀錄變化值
            norm = 0  # 標準化
            tmp = {}
            # 計算authority
            tmp = self.authority.copy()
            for node in self.graph.nodes():
                self.authority[node] = 0
                for incident_page in self.graph.incidents(node):  # 遍历所有“入射”的页面
                    self.authority[node] += self.hub[incident_page]
                norm += pow(self.authority[node], 2)
            # 標準化
            norm = math.sqrt(norm)
            for node in self.graph.nodes():
                self.authority[node] /= norm
                change += abs(tmp[node] - self.authority[node])

            # 計算hub
            norm = 0
            tmp = self.hub.copy()
            for node in self.graph.nodes():
                self.hub[node] = 0
                for neighbor_page in self.graph.neighbors(node):  # 遍历所有“出射”的页面
                    self.hub[node] += self.authority[neighbor_page]
                norm += pow(self.hub[node], 2)
            # 標準化
            norm = math.sqrt(norm)
            for node in self.graph.nodes():
                self.hub[node] /= norm
                change += abs(tmp[node] - self.hub[node])

            if change < self.min_delta:
                flag = True
                break

        print("The best authority page: ", max(self.authority.items(), key=lambda x: x[1]))
        print("The best hub page: ", max(self.hub.items(), key=lambda x: x[1]))


if __name__ == '__main__':

    start = time.clock()
    f = open('graph_6.txt', 'r')
    dg = digraph()

    # 取得邊
    edges = [line.strip('\n').split(',') for line in f]

    # 取得點
    nodes = []
    for edge in edges:
        if edge[0] not in nodes:
            nodes.append(edge[0])
        if edge[1] not in nodes:
            nodes.append(edge[1])
    # print(nodes)
    dg.add_nodes(nodes)

    for edge in edges:
        dg.add_edge((edge[0], edge[1]))
    
    # print(dg)
    hits = HITSIterator(dg)
    hits.hits()
    end = time.clock()
    print('cost time:',end-start)
