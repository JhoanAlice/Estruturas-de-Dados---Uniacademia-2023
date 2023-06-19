# Author: Luiz Thadeu Grizendi
# UniAcademia - Juiz de Fora
# Minas Gerais - Brasil

global DEFAULT_CAPACITY
DEFAULT_CAPACITY=100

class arrayList(object):
     """Represents a singly array list."""
     def __init__(self, capacity=None):
          """Instantiates a array list with a default capacity
             if capacity=None
          """
          if capacity:
              if not isinstance(capacity,int):
                   raise TypeError('capacity is integer')
          else:
              capacity = DEFAULT_CAPACITY # default capacity
          self._array = [None] * capacity
          self._size = 0

     def __len__(self):
          """ Length of the arrayList"""
          return self._size

     def __str__(self):
          """ The string representation of the arrayList"""
          return str(self._array[0:len(self)])

     def __repr__(self):
          """ The representation of the arrayList """
          return "{0} ({1})".format(self.__class__.__name__, self)
     
     def __iter__(self):
          """ Supports traversal with a for loop"""
          return iter(self._array[0:len(self)])
     
     def __getitem__(self, index=-1):
          """ Subscript operator for access at index"""
          return self._array[0:len(self)][index]
     
     def __setitem__(self, index, value):
          """ Subscript operator for replacement at index"""
          self._array[index] = value

     def clear(self):
          """ clear data"""
          self.__init__(len(self._array))

     def insert(self, index, value):
          """ insert value at index"""
          if self._size == len(self._array):
               self._sizeIncreament()
          if index > self._size:
               index=self._size
          #Shift items down by one position
          for i in range(self._size, index, -1):
               self._array[i] = self._array[i - 1]
          # Add new item and increment logical size
          self._array[index] = value
          self._size += 1

     def remove(self, index):
          """ remove value at index"""
          # Shift items up by one position
          for i in range(index, self._size  - 1):
               self._array[i] = self._array[i + 1]
          # Decrement logical size
          self._size  -= 1
          
     def _sizeIncreament(self):
          """auxiliary method size Increament"""
          temp = arrayList(len(self._array) * 2) # Create a new array
          for i in range(self._size): # Copy data from the old
               temp [i] = self._array[i] # array to the new array
          self._array = temp # Reset the old array variable to the new array
          
if __name__ == '__main__':
     a=arrayList(10)
     a.insert(0,10)
     a.insert(4,20)
     a.insert(4,30)
     print(a)
     a.remove(2)
     print(a)
     
     






















