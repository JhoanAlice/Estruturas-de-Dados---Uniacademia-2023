def reverse(a):
     rev =  []
     for e in a:
          rev.insert(0,e)
     return rev

from math import inf
def bigger(a):
     big =  -inf
     for e in a:
          if e>big:
               big=e
     return big

def smaller(a):
     smal =  inf
     for e in a:
          if e<smal:
               smal=e
     return smal

if __name__ == '__main__':
     L = [10,20,30,50]
     print('lista original ',L)   
     print('lista reversa ',reverse(L))    # ativou a função local reverse
     print('lista reversa com o uso do iterator reversed ', [e for e in reversed(L)])
     # ativou o método reversed nativo da estrutura list
     # que retorna um iterator dos elementos em ondem inversa
     print('lista reversa usando slice ',L[::-1])      
     L.reverse()  # ativa o método reverse() da clasee list
     # Obs :  esse método modifica a ordem da lista inicial, para ordem reversa
     #        dos elementos 
     print('lista reversa com o uso do método reverse() aplicado na class')
     print(L)
     print(bigger(L))     
     print(max(L))     
     print(smaller(L))     
     print(min(L))     

          
          
