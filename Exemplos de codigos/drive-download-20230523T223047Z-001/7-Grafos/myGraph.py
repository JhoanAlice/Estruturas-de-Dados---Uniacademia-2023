# https://www.bogotobogo.com/python/python_graph_data_structures.php
#  Adapted by Luiz Thadeu Grizendi
class Vertex:
    def __init__(self, ID):
        self.id = ID
        self.adjacent = {}  # dict()

    def __str__(self):
        #return self.id
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self): # return [(Vextex,weight)]
        return self.adjacent.items()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
     
    def __init__(self,directed = True, vertices = None, edges = None):
        self.directed = directed 
        self.vert_dict = {} # dict()
        self.num_vertices = 0
        if vertices:
             for v in vertices:
                  self.add_vertex(v)
        if edges:
             for u,v,weight in edges:
                  self.add_edge(u,v,weight)                       

    def __iter__(self):
        return iter(self.vert_dict.values())
     
    def __str__(self):
         s = ''
         for v in self:
              s += str(v.get_id()) + ' : '
              for neighbor,weight in v.get_connections():
                      s += str((neighbor.get_id(), weight))+','
              if s:
                   s = s[:-1]+'\n'                   
         return s

    def __repr__(self):
         s = '{\n'
         for v in self:
              s += '     '+str(v.get_id()) + ' : {'  
              for neighbor,weight in v.get_connections():
                      s += str(neighbor.get_id())+':'+str(weight)+', '
              if s[-1]=='{':
                  s += '}\n'
              else:
                  s = s[:-2]+'}\n'
         s += '}'
         return s

    def add_vertex(self, ID):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(ID)
        self.vert_dict[ID] = new_vertex
        return new_vertex

    def get_vertex(self, ID):
        if ID in self.vert_dict:
            return self.vert_dict[ID]
        raise KeyError('vertex does not exist')
    
    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
 
        if to not in self.vert_dict:
            self.add_vertex(to)
            
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        if not self.directed:
             self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def vertices(self):
        return list(self.vert_dict.keys())

    def edges(self):
        tr = list();
        for v in self:
            c = str(v.get_id())
            #s += str(v.get_id()) + ' : '
            for neighbor,weight in v.get_connections():
                  tr.append((c,neighbor.get_id(), weight))
        return tr

    def get_edge(self, u,v):
        if u in self.vert_dict:
            uu = self.get_vertex(u)
            if v in self.vert_dict:
                vv = self.get_vertex(v)
                return uu.adjacent.get(vv)
        raise KeyError('edge does not exist')

    def incidents(self, v): # return  [( ? , v )] 
        incidentList = []
        for u,vv,w in self.edges():
            if (vv == v):
                incidentList.append((u,w))
        return incidentList
    
    def successors(self, u): # return  [( u , ? )]
         tr = []
         for source in self:
              if  u == source.get_id():
                   for neighbor,weight in source.get_connections():
                        tr.append((neighbor.get_id(), weight))
                   break
         return tr 
        
if __name__ == '__main__':

    g = Graph(True,['a','b','c','d','e','f'],[('a', 'b', 7),('a', 'c', 9),('a', 'f', 14),\
                    ('b', 'c', 10),('b', 'd', 15),('c', 'd', 11),('c', 'f', 2),('d', 'e', 6), \
                    ('e', 'f', 9),('f', 'a', 99)])                          
    """
    g = Graph(True)
    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')
    g.add_edge('a', 'b', 7)  
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)
    """
    
    print(g)
    print('sucessores de a : ',g.successors('a'))
    print('sucessores de c : ',g.successors('c'))
    print('incedentes em c : ',g.incidents('c'))

    print('vertices : ',g.vertices())
    print('edges : ',g.edges())

    
