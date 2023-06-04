
class pessoa(object):
     def __init__(self,nome,rg,idade,sexo):
          self.nome = nome
          self._id = rg
          self.__idade = idade
          self.sexo = sexo
          print(self.__getNome())
          
     def getIdade(self):
          return self.__idade

     def __getNome(self):
          return self.nome

class cliente(object):
     def __init__(self,mat,nome):
          self.mat = mat
          self.nome = nome

if __name__ == '__main__':        
     p1 = pessoa('Luiz','123',34,'M')
     p2 = pessoa('Ana','223',30,'F')
     print(p2.getIdade())
     print(p2._id)


