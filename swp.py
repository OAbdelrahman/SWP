from cmath import inf
import numpy as np


def loadGraph (edgeFilename):
    nodes= []
    edges= []
    adj_list= {}

    with open(f"{edgeFilename}") as file:
        for i in file:
            edge =[int(i) for i in i.split()]
            edges.append(edge)

            for j in edge:
                nodes.append(j)
        
        nodes = np.unique(np.array(nodes))

    for node in nodes:
        adj_list[node] = []
    
    for u,v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
        
 
    return adj_list

class MyQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        return self.queue.append(x)
        

    def dequeue(self):
        return self.queue.pop(0)

    def is_empty(self):
        if len(self.queue):
            return False
        else:
            return True

    def print_queue(self):
        return str(self.queue)


def BFS(G,s):
    Q = MyQueue()
    d = []
    
    for u in G:
        d.append(inf)
    
    d[s]= 0
    
    Q.enqueue(s)
    
    while not Q.is_empty():
        u = Q.dequeue()
        for v in G[u]:
            if d[v]== inf:
                d[v]= d[u]+1
                Q.enqueue(v)
                
    return d

def distanceDistribution(G):
    dist = {}

    for i in range(11):
        dist[i]=0

    for i in G:
        for j in BFS(G,i):
            dist[j]+=1
    
    tot = 0
    for k in dist:
        tot+= dist[k]
    
    for m in dist:
        if dist[m] != 0:
            dist[m]= round(((dist[m]-len(G))/tot)*100, 1)
    
    return dist
    

def main ():
    G = loadGraph("edges.txt")
    print(distanceDistribution(G))


if __name__ == "__main__":
    main()

    # The distribution results show that 97.8% of the nodes
    # are within 6 degrees of separation from the source node.
    # That is pretty significant as far as the SWP is concerned.