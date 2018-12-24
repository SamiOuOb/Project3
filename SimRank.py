import numpy as np
import time

def simrank(G,C,n,t=10):
    S = np.identity(n)
    I = np.identity(n)
    G = normalize(G)
    i = 1
    while True:
        S = C * np.dot(np.dot(G.T,S),G) + (1-C) * I
        for j in range(n):
            S[j][j] = 1
        if i >= t:
            break
        i += 1
    return S

def normalize(G):
    s = G.sum(0)
    return G/s

if __name__ == '__main__':
    start = time.clock()
    
    C = 0.8
    # 取得邊
    f = open('graph_5.txt', 'r')
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
 
    # 生成矩陣
    G = np.zeros([N, N])

    for edge in edges:
        G[edge[1]-1, edge[0]-1] = 1
    # print(G)
    float_formatter = lambda x:"%.2f" % x
    np.set_printoptions(formatter={'float_kind':float_formatter})
    S = simrank(G,C,N)
    S=np.nan_to_num(S)
    print((S))

    end = time.clock()
    print('cost time:',end-start)