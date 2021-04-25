from collections import defaultdict

#Graph Class
class graph:
  def __init__(self,vertices):
    self.Graph=defaultdict(list) #Dictionary Containing Adjency list
    self.V = vertices #No of Verticies



  #Add edge Function
  def addEgde (self,u,v):
    self.graph[u].append(v)

  #Recursion Topological
  def TopologicalSort(self,v,visited,stack):

    #Current node visited
    visited[v] = True

    #all Verticies
    for i in self.Graph[v]:
      if visited == False:
        self.Topological(i,visited,stack)
    
    #pushing vertex current into stack
    stack.insert(0,v)

  def Topological_1(self):

    #Mark all vertices as non visited
    visited= [False]* self.V 
    stack = []

    for i in range(self.V):
      if visited[i] == False:
        self.TopologicalSort(i,visited,stack)

print stack 
