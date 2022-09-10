
from collections import defaultdict


class Graph:

    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)
        self.end = False
        self.rob = False
        self.length = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def checkCycle(self):
        visited = [False for i in range(self.v)]
        length = 0
        for i in range(self.v):
            if visited[i] == False:
                if self.dfs(i, visited, -1) == True:

                    if self.length >= 4:
                        self.rob = True
                    self.length = 0

    def dfs(self, i, visited, parent):
        visited[i] = True
        for j in self.graph[i]:


            if self.end:
                self.length = 0


            if visited[j] == False:
                self.length += 1
                if self.dfs(j, visited, i):
                    return True


            elif parent != j:
                return True

        self.end = True
        return False

g = Graph(9)
g.addEdge(0, 1)
g.addEdge(3, 2)
g.addEdge(2, 2)
g.addEdge(2, 3)
g.addEdge(7, 4)
g.addEdge(3, 5)
g.addEdge(3, 4)
g.addEdge(5, 8)
g.addEdge(6, 2)
g.addEdge(3, 7)
g.addEdge(7, 8)
g.checkCycle()
if g.rob:
    print("Robber wining graph")
else:
    print("Cop wins")
