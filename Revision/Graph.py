class Graph:
    def __init__(self):
        self.graph={}
    def Add_Vertex(self,Vertex):
        if Vertex not in self.graph:
            self.graph[Vertex]=[]

    def Add_Edge(self,u,v):
        if u not in self.graph:
            self.Add_Vertex(u)
        if v not in self.graph:
            self.Add_Vertex(v)
        self.graph[u].append(v)
        self.graph[v].append(u)

    def Display(self):
        for i in self.graph:
            print(i,'->',self.graph[i])
    def Remove_Edge(self,u,v):
        self.graph[u].remove(v)






# class Graph:
#     def __init__(self):
#         self.graph={}
#
#     def Add_Vertex(self,Vertex):
#         self.graph[Vertex]=[]
#     def Add_Edge(self,u,v):
#         if u not in self.graph:
#             self.Add_Vertex(u)
#         if v not in self.graph:
#             self.Add_Vertex(v)
#         self.graph[u].append(v)
#         self.graph[v].append(u)
#
#     def Display(self):
#         for i in self.graph:
#             print(i,"->",self.graph[i])

# class Graph:
#     def __init__(self):
#         self.graph = {}
#
#     def add_vertex(self, vertex):
#         if vertex not in self.graph:
#             self.graph[vertex] = []
#
#     def add_edge(self, u, v):
#         if u not in self.graph:
#             self.add_vertex(u)
#         if v not in self.graph:
#             self.add_vertex(v)
#         self.graph[u].append(v)
#         self.graph[v].append(u)
#     def Remove_Edge(self,u,v):
#         self.graph[u].remove(v)
#
#     def display(self):
#         for vertex in self.graph:
#             print(vertex, "->", self.graph[vertex])


# Example usage:
g = Graph()
g.Add_Edge('A', 'B')
g.Add_Edge('A', 'C')
g.Add_Edge('B', 'D')
g.Add_Edge('C', 'D')
g.Add_Edge('D', 'E')
# g.Remove_Edge('A','C')
g.Display()




