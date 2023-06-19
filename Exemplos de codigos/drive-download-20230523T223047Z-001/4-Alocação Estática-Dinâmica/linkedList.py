# Author: Luiz Thadeu Grizendi
# UniAcademia - Juiz de Fora
# Minas Gerais - Brasil

class Node(object):
     """Represents a singly linked node."""
     def __init__(self, value, next = None):
          """Instantiates a Node with a default next of None."""
          self.value = value
          self.next = next
     def __str__(self):
          return str(self.value)+'-->'+str(self.next)
     def __repr__(self):
          return str(self)
     
class linkedList(object):
     """Represents a singly linked list."""
     def __init__(self):
          """Instantiates a linked list with a default head of None and size zeroe"""
          self._size = 0
          self._head = None
          
     def __str__(self):
          """ The string representation of the linkedList"""
          return str([e for e in self])

     def __len__(self):
          """ Length of the list"""
          return self._size

     def __repr__(self):
          """ The representation of the linkedList"""
          return "{0} ({1})".format(self.__class__.__name__, self)
     
     def __iter__(self):
          """ Supports traversal with a for loop"""
          self.__current = self._head
          return self
     
     def __next__(self):
          if self.__current == None:
               raise StopIteration
          else:
            previous = self.__current
            self.__current = self.__current.next 
            return previous.value

     def __getitem__(self, index=-1):
          """ Subscript operator for access at index"""
          probe = self._head
          while index > 0 and probe.next != None:
               probe = probe.next
               index -= 1
          return probe.value
     
     def __setitem__(self, index, value):
          """ Subscript operator for replacement at index"""
          probe = self._head
          while index > 0 and probe.next != None:
               probe = probe.next
               index -= 1
          probe.value = value
     
     def clear(self):
          """ clear data"""
          self.__init__()

     def addFirst(self, value):
          """add value first position"""
          self._head = Node(value, self._head)
          self._size += 1
          
     def addLast(self, value):
          """add value Last position"""
          newNode = Node(value)
          if self._head is None:
               self._head = newNode
          else:
               current = self._head
               while current.next != None:
                    current = current.next
               current.next = newNode
          self._size += 1
          
     def insert(self, index, value):
          """add value in to position index"""
          if self._head is None or index <= 0:
               self._head = Node(value, self._head)
          else:
               # Search for node at position index - 1 or the last position
               current = self._head
               while index > 1 and current.next != None:
                    current = current.next
                    index -= 1
               # Insert new node after node at position index - 1
               # or last position
               current.next = Node(value, current.next)
          self._size += 1

     def removeFirst(self):
          """remove first"""
          if self._head:
               removedItem = self._head.value
               self._head = self._head.next
               self._size -= 1
               return removedItem
          raise IndexError('remove from empty list')
          
     def removeLast(self):
          """remove last"""
          if self._head:
               current = self._head
               while current.next != None:
                    previous = current
                    current = current.next
               removedItem = current.value
               previous.next = None
               self._size -= 1
               return removedItem
          raise IndexError('remove from empty list')
          

     def remove(self, index):
          """remove value in to position index"""
          if self._head.next is None:
               raise IndexError('remove from empty list ')
          if index <= 0: # remove fisrt
               return self.removeFirst()
          # Search for node at position index - 1 or
          # the next to last position
          current  = self._head
          while index > 1 and current.next.next != None:
               current  = current.next
               index -= 1
          removedItem = current.next.value
          current.next = current.next.next
          self._size -= 1
          return removedItem


     


