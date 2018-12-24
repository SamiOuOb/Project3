
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import time
 
 
if __name__ == '__main__':
    
    start = time.clock()
    # 取得邊
    f = open('graph_1.txt', 'r')
    edges = [line.strip('\n').split(',') for line in f]
    # print(edges)

    # 取得點
    nodes = []
    for edge in edges:
        if edge[0] not in nodes:
            nodes.append(edge[0])
        if edge[1] not in nodes:
            nodes.append(edge[1])
    # print(nodes)
 
    N = len(nodes) #點數量
 
    # to int
    i = 0
    node_to_num = {}
    for node in nodes:
        node_to_num[node] = i
        i += 1
    for edge in edges:
        edge[0] = node_to_num[edge[0]]+1
        edge[1] = node_to_num[edge[1]]+1
    # print(edges)
 

    G = nx.DiGraph()
    for edge in edges:
            
    
    # nx.draw(G, with_labels=True)
    # plt.show()

    import matplotlib.pyplot as plt
    import networkx as nx

    layout = nx.spring_layout(G)
    pr=nx.pagerank(G,alpha=0.85)
    # print(pr)
    for node, pageRankValue in pr.items():
        print("%d,%.4f" %(node,pageRankValue))
    plt.figure(1)
    nx.draw(G, pos=layout, node_size=[x * 6000 for x in pr.values()],node_color='0.65',with_labels=True)
    end = time.clock()
    print('cost time:',end-start)
    plt.show()