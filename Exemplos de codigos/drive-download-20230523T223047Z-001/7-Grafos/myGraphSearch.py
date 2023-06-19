# Author: Luiz Thadeu Grizendi
# UniAcademia - Juiz de Fora MG, Brasil
import sys
sys.path.append('../Collections')
from stack import stack
from Queue import Queue as queue
from binHeap import minHeap as priorityQueue

from myGraph import * 

def breadth_first_search(graph,initial):
   frontier = queue()  
   frontier.enqueue(initial)     
   explored = list()
   while not frontier.isEmpty():
       curr = frontier.dequeue()
       explored.append(curr)
       for child,weight in graph.successors(curr):
            if child not in frontier and child not in explored:
                 frontier.enqueue(child)
   return explored

def depth__first_search(graph,initial):
   frontier = stack()  
   frontier.push(initial)     
   explored = list()
   while not frontier.isEmpty():
       curr = frontier.pop()
       explored.append(curr)
       for child,weight in reversed(graph.successors(curr)):
            if child not in frontier and child not in explored:
                 frontier.push(child)
   return explored

def dijkstra(graph, start):
     # Initialize both vertices, distance and previous list
     vertices = graph.vertices()
     n = len(vertices) # vertices list lenght
     dist = [float('inf')] * n 
     previous = [None] * n # for path  
     i = vertices.index(start)
     dist[i] = 0	# Distance from start to current
     
     Q = priorityQueue()
     # Initialize PriorityQueue (0,start) another all( inf, current)          
     for v in vertices:
          Q.insert(tuple([float('inf'),v]))
     i = Q.indexValue(start)
     Q.update(i,tuple([0,start]))

     while not Q.isEmpty():	# main loop
          d,u = Q.delMin()  # tuple(distance,vertex)
          i = vertices.index(u)
          dist[i] = d  # distance                  
          for child,weight in graph.successors(u): # where v has not yet been removed from Q
               k = vertices.index(child)
               dist_between = weight  #  dist_between u v
               alt = dist[i] + dist_between
               j = Q.indexValue(child)
               if j == -1:  # Vertex not in Q
                    continue
               dist[k],v = Q.get(j) # Q.queue[j] = (distance,vertex)

               if alt < dist[k]:
                    dist[k] = alt
                    Q.update(j,tuple([dist[k],child])) # Updtade tuple in Queue
                    previous[k] = u
   
     return previous,dist

if __name__ == '__main__':
    vertices = ['a','b','c','d','e','f']
    edges = [('a', 'b', 7),('a', 'c', 9),('b', 'd', 14),('b', 'e', 10),('c', 'f', 15),]
    g = Graph(True,vertices,edges)
    print(g)
    """  
    e=breadth_first_search(g,'a')
    print('Explored ',e)
    """
    e=depth__first_search(g,'a')
    print('Explored ',e)
    """
    vertices = [1,2,3,4,5,6,7,8]
  
    edges = [(5,4,150),(5,6,25),(6,7,90),(6,4,100),(6,8,140),(4,3,120), \
             (3,2,80),(3,1,100),(2,1,30),(8,1,170),(7,8,100)]

    g = Graph(True,vertices,edges)
    p,d=dijkstra(g,5)
    print('path','dist')
    i = 0
    for u in vertices:
       v = p[u-1]
       path = str(u)+'>-'
       while v:
          path+=str(v)+'>-'
          v = p[v-1]
       if path:
          path = path[:-2]      
       print(path[::-1],d[i])
       path = ''
       i +=1 
       
   """


     
