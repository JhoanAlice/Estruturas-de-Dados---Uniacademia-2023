from myGraph import Graph 

class partida:
     def __init__(self,rodada,dt,placar):
          self.rodada =rodada
          self.dt = dt
          self.placar = placar

     def __str__(self):
          if self.placar:
               return 'rodada: '+str(self.rodada)+', data : '+ str(self.dt)+ \
                      ','+ 'placar : ' + str(self.placar)
          return 'rodada: '+str(self.rodada)+', data : '+ str(self.dt)+ \
                      ','+ 'placar :  x '
          

class brasileirao:
     def __init__(self,ano = 2023,times=None,partidas=None):
          """ano: inteiro, times:lista de times,
             partidas: [(mandante,visitante,placar)]"""
          self.ano = ano
          self.tabela = Graph()
          if times:
               self.init_times(times)
          if partidas:
               self.init_partidas(partidas)
               
     def init_times(self,times):
          """ Inicializa todos os times como vértices do grafo"""          
          for time in times:
               self.tabela.add_vertex(time)
          
     def init_partidas(self,partidas):
          """ Inicializa todas as partidas com a data prevista da partida e
          colocar None no placar simbolizando que a partida ainda não ocorreu
          m:mandante v:visitante, p:placar"""
          for m,v,p in partidas:
               self.tabela.add_edge(m,v,p) 

     def __str__(self):
          return str(repr(self.tabela))

     def __repr__(self):
          return repr(self.tabela)
     
     def jogoconcluido(self,time_mandante,time_visitante,partida):
          # Alterar os dados da partida com a data e placar
          # partida é uma instância da classe 
          # self.tabela.add_edge('fla','flu',partida) <-- seguir esse exemplo
          # cuidado a partida passada como parâmetro é uma classe
          # nela vc tem a rodada (string) data (string) e, o placar string
          pass

     def jogos_time(self,time):
          # listar os jogos do time informado
          # obter os sucessores do time
          # obter os incidentes com o time
          tr = []
          for v,p in self.tabela.successors(time):
               tr.append((time,v,str(p)))
          for m,p in self.tabela.incidents(time):
               tr.append((m,time,str(p)))
          return tr     
          #pass

     def jogos_rodada(self,rodada):
          # listar os jogos da rodada informada
          pass

     def jogos_que_faltam_time(self,time):     
          # listar os jogos que ainda faltam do time informado
          # obter os sucessores do time e comparar com a lista de vértices,
          # isto é, obter os vértices que não são sucessores do time
          # obter os incidentes com o time e comparar com a lista de vértices,
          # isto é, obter os vértices que não tem como incidente o time
          pass
     
     def jogos_dt(self,dt):
          # listar os jogos da data informada
          # para cada vértice obter todos os seus sucessores e verificar
          # se a data informada é igual a data gravada
          pass     

     def placar_jogo(self,time_mandante,time_visitante):
          # obter o placar de um jogo realizado
          # caso o placar seja == ' ' retornar ' x '
          pass

     def data_jogo(self,time_mandante,time_visitante):
          # obter a data de um jogo 
          pass

     def times(self):
          # listar os times 
          pass

     def partidas(self):
           # listar todas as partidas 
          pass

if __name__ == '__main__':
     b = brasileirao(2023,['fla','flu','bot'],\
                     [['flu','fla',partida('1','20/03/2023','1x0')],\
                      ['fla','flu',partida('3','14/05/2023','0x3')],\
                      ['flu','bot',partida('5','12/05/2023','4x0')]])

     
     b.init_partidas([['flu','fla',partida('1','20/03/2023','1x0')],\
                      ['bot','flu',partida('10','12/09/2023',None)]])
     
     b.init_times(['flu','fla','bot'])
     
                  
