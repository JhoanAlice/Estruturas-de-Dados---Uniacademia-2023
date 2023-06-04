class deque:
       def __init__(self,iterable=None):
         self.__items = []
         if iterable:
              for item in iterable:
                   self.addRear(item)        
       def addFront(self, item):
           self.__items.insert(0,item)   
       def addRear(self, item):
           self.__items.append(item)   
       def removeFront(self):
           if len(self) == 0:
              raise IndexError('remove from empty deque')         
           return self.__items.pop(0)   
       def removeRear(self):
           if len(self) == 0:
              raise IndexError('remove from empty deque')
           return self.__items.pop()
       def rear(self):
           if len(self) == 0:
              raise IndexError('rear from empty deque')
           return self.__items[-1]
           #return self.__items[llen(self)-1]
       def front(self):
           if len(self) == 0:
              raise IndexError('front from empty deque')
           return self.__items[0]
       def clear(self):
          self.__init__()
       def isEmpty(self):
           return len(self) == 0   
       
       def __repr__(self):
           return 'front -> ['+', '.join([str(item) for item in self]) +'] <- rear'
          
       def __len__(self):
           return len(self.__items)

       def __str__(self):
           return str(list(self))
 
       def __contains__(self,key):
           return key in self.__items
       
       def __iter__(self):
              return iter(self.__items)

if __name__ == '__main__':

     d=deque()
     print(d.isEmpty())
     print(repr(d))     
     d.addRear(40)
     d.addRear(50)
     d.addFront(20)
     d.addFront(10)
     print(d)
     print('front ',d.front())
     print('rear ',d.rear())

     print(repr(d))     
     print(len(d))
     print(d.isEmpty())
     d.addRear(70)
     print('remove Rear',d.removeRear())
     print('remove Front',d.removeFront())
     print(d)
