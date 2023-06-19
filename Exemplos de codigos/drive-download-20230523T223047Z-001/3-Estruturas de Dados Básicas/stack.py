class stack:                                                                                                                                       
     def __init__(self,iterator=None):
         self.__items = []
         if iterator:
              for item in iterator:
                   self.push(item)
     def clear(self):
         self.__items = []
     def isEmpty(self):
         return len(self) == 0
     def push(self, item):
         self.__items.append(item)         
     def extend(self,list):
         for element in list:
              self.push(element)
     def pop(self):
         return self.__items.pop(-1)
         #return self.__items.pop(len(self)-1)
     def top(self):
         return self.peek()          
     def peek(self):
         return self.__items[-1]
         #return self.__items[len(self)-1]

     def __contains__(self,key):
        return key in self.__items
     def __len__(self):
        return len(self.__items)
     def __str__(self):
        return '['+', '.join([str(v) for v in self]) +']'
     def __repr__(self):
          return str(self)
     def __iter__(self):
          self.__current = len(self)-1
          return self     
     def __next__(self):
          if self.__current < 0:
               raise StopIteration
          else:
               self.__current -= 1
               return self.__items[self.__current + 1]

if __name__ == '__main__':
     s = stack()
     print('top (top) ',s.peek() if not s.isEmpty() else 'stack Empty!!!')
     s.push(40)
     s.push(20)
     s.push(10)
     print(repr(s)) # call __repr__ 
     print(s) # call __str__
     print('size ',len(s))
     print('top (top) ',s.top())
     print('remove top ',s.pop())
     print('top (peek)',s.peek())
     print(10 in s)
     print('size ',len(s))
     for e in s:
          print(e)
