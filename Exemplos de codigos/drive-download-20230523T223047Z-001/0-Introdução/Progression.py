import abc
import math

class Progression(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def setFirst(self,first):
         pass                                  
    @abc.abstractmethod
    def setBase(self,base):
      	 pass
    @abc.abstractmethod    
    def getFirst(self):
       	 pass
    @abc.abstractmethod
    def getBase(self):
       	 pass                
    @abc.abstractmethod
    def sumTerms(self,n): 
        pass
    @abc.abstractmethod
    def generalTerm(self,n):
        pass
    @abc.abstractmethod
    def interpolation(f, l, n):
        pass
    @abc.abstractmethod
    def get_first_base(i,ai,j,aj):
        pass

    @abc.abstractmethod
    def show(self, n):
        pass

    
class abstractProgression(Progression):
    def __init__(self,base = None, first = None):
         self._base = base  # Razão da Progressão
         self._first = first # primeiro termo da Progressão

    def setFirst(self,first):
         self._first=first

    def setBase(self,base):
         self._base = base   

    def getFirst(self):
         return self._first   

    def getBase(self):
         return self._base
        
    def show(self,n):
        tr=''
        for i in range(1,n+1):
            tr+=str(self.generalTerm(i))+', '
        return tr[0:-2]
    
class arithmeticProgression(abstractProgression):                  
     def __init__(self,base = None, first = None):
          super().__init__(base,first)

     def generalTerm(self,n):
          return self.getFirst()+(n-1)*self.getBase()

     def sumTerms(self,n):
          return ((self.getFirst()+self.generalTerm(n))*n/2)    

     @staticmethod
     def interpolation(ai, aj, n):
          b=(aj-ai)/(n+1)
          l = [ai]
          for i in range(0, n):
               ai += b
               l.append(ai)
          l.append(aj)     
          return l

     @staticmethod
     def get_first_base(i,ai,j,aj):
          i -= 1
          j -= 1
          base=(aj-ai)/((j-i-1)+1)
          return ai- base*(i), base

class geometricProgression(abstractProgression):                                            
     def __init__(self,base = None, first = None):
          super().__init__(base,first)
          
     def generalTerm(self,n):
          return self.getFirst()*math.pow(self.getBase(),n-1)

     def sumTerms(self,n):
          if self.getBase() > 0 and  self.getBase() < 1:
               return self.getFirst()/(1-self.getBase())
          else:    
               return (self.getFirst()*(math.pow(self.getBase(),n)-1)/(self.getBase()-1))

     @staticmethod
     def get_first_base(i,ai,j,aj):
          i -= 1
          j -= 1
          base=math.pow(aj/ai, 1/(j-i))
          return ai/ base**(i), base

     @staticmethod
     def interpolation(ai, aj, n):
          b=math.pow(aj/ai,math.pow(n+1,-1))
          l = [ai]
          for i in range(0, n):
               ai *= b
               l.append(ai)
          l.append(aj)
          return l
     
if __name__ == '__main__':
    print('PA r = 2, a1 = 1')
    pa = arithmeticProgression(2,1)
    print('5 termos da PA : ',pa.show(5))
    print('a5 = ',pa.generalTerm(5))
    print('S5 = ',pa.sumTerms(5))
    print('Interpolar [1,..,..,..,9] ',arithmeticProgression.interpolation(1,9,3))
    print('first,base PA a3 = 8, a6 = 17')
    f,b = arithmeticProgression.get_first_base(3,8,6,17)
    print('a1 = ',f,'r : ',b)
    print('----------------------------------')
    print('PG q = 2, a1 = 1')
    pg = geometricProgression(2,1)
    print('5 termos da PG : ',pg.show(5))
    print('a10 = ',pg.generalTerm(10))
    print('S4 = ',pg.sumTerms(4))
    print('Interpolar [1,..,..,..,81] ',pg.interpolation(1,81,3))
    print('first,base PG a3 = 9, a5 = 81')
    f,b = geometricProgression.get_first_base(3,9,5,81)
    print('a1 = ',f,'r : ',b)
    

