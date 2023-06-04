class Queue:
     def __init__(self,iterable=None):
         self.__items = []
         if iterable:
              for item in iterable:
                   self.enqueue(item)

     def clear(self):
          self.__init__()

     def isEmpty(self):
          return len(self) == 0

     def enqueue(self, item): 
          self.__items.append(item)
     def offer(self, item):  
          self.enqueue(item)
	  
     def dequeue(self):  
          if len(self) == 0:
              raise IndexError('dequeue/poll from empty queue')
          return self.__items.pop(0)

     def poll(self):
          """the same as dequeue"""
          return self.dequeue()

     def peek(self):  
          if len(self) == 0:
              raise IndexError('peek/front from empty queue')
          return self.__items[0]

     def front(self):
          """the same as peek"""
          return self.peek()
     
     def extend(self,iterable):
          for element in iterable:
               self.enqueue(element)
               
     """native python functions"""
     def __contains__(self,key):
          return key in self.__items
     
     def __len__(self):
          return len(self.__items)

     def __str__(self):
          return str(self.__items) 
 
     def __repr__(self):
          return 'Queue->'+repr(self.__items)

     def __iter__(self):
          return iter(self.__items)

     def __eq__(self, iterable):
        "Test self==iterable"
        return list(self) == list(iterable)
    
     """    
     def __iter__(self):
          self.__current = 0
          return self

     def __next__(self):
          if self.__current >= len(self):
               raise StopIteration
          else:
               self.__current += 1
               return self.__items[self.__current - 1]
     """
if __name__ == '__main__':
     
     q=Queue()	
     q.enqueue(10)
     q.offer(20)
     q.enqueue(30)
     q # call __repr__
     print(q) # call __str__
     print('peek/front ',q.peek())
     print('peek/front ',q.front())

     print('dequeue/pool ',q.dequeue())
     print('peek/front ',q.peek())
     print('dequeue/pool ',q.poll())
     print(len(q))
     for e in q:
          print(e)
     
