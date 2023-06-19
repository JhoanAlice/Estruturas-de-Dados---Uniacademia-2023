# Author: Luiz Thadeu Grizendi
# UniAcademia - Juiz de Fora MG, Brasil
# adapted from https://runestone.academy/runestone/books/published/pythonds/Trees/BinaryHeapImplementation.html
class binHeap:
    def __init__(self):
        self._heapList = [0]
        self._currentSize = 0

    def insert(self,element):
        self._heapList.append(element)
        self._currentSize = self._currentSize + 1
        self._percUp(self._currentSize)
        #self.buildHeap(self._heapList[1:]+[element])
        
    def remove(self,element):
        self._heapList.remove(element)
        self.buildHeap(self._heapList[1:])

    def extend(self,alist):
        self._heapList  
        self._currentSize = len(self._heapList)
        self.buildHeap((self._heapList + alist[:])[1:])

    # for updating an element in the heap 
    def update(self, i, element):        
        self._heapList[i] = element 
        self.buildHeap(self._heapList[1:])

    # for checking if the heap is empty 
    def isEmpty(self): 
        return len(self._heapList) <= 1
  
    # for checking if the heap is empty 
    def index(self,element):
        return self._heapList.index(element)

    def get(self,index):
        return self._heapList[index]

    # for checking if the heap is empty 
    def indexValue(self,element):
        for i in range(1,len(self._heapList)):
            if element == self._heapList[i][1]:
                return i
        return -1

    def get(self,index):
        return self._heapList[index]

    def clear(self):
        self._heapList = [0]
        self._currentSize = 0       
    
    def copy(self):
        if isinstance(self, maxHeap):
            h = maxHeap()
        else:
            h = minHeap()        
        h.buildHeap(self._heapList[1:])
        return h
    
    def __contains__(self,element): 
        return element in self._heapList
    
    def contains(self,element): 
        return element in self

    def __len__(self,element): 
        return len(self._heapList)-1

    def __iter__(self): 
        return iter(self._heapList[1:])

    def __repr__(self): 
        return repr(self._heapList[1:])

    def __str__(self): 
        return str(self._heapList[1:])
    

class minHeap(binHeap):

    def __init__(self):
        super().__init__()

    def __min__(self):
        return self._heapList([1]) if not self.isEmpty else None

    def _percUp(self,i):
        while i // 2 > 0:
          if self._heapList[i] < self._heapList[i // 2]:
             tmp = self._heapList[i // 2]
             self._heapList[i // 2] = self._heapList[i]
             self._heapList[i] = tmp
          i = i // 2

    def _percDown(self,i):
      while (i * 2) <= self._currentSize:
          mc = self._minChild(i)
          if self._heapList[i] > self._heapList[mc]:
              tmp = self._heapList[i]
              self._heapList[i] = self._heapList[mc]
              self._heapList[mc] = tmp
          i = mc

    def _minChild(self,i):
      if i * 2 + 1 > self._currentSize:
          return i * 2
      else:
          if self._heapList[i*2] < self._heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
        retval = self._heapList[1]
        self._heapList[1] = self._heapList[self._currentSize]
        self._currentSize = self._currentSize - 1
        self._heapList.pop()
        self._percDown(1)
        return retval

    def buildHeap(self,alist):
        i = len(alist) // 2
        self._currentSize = len(alist)
        self._heapList = [0] + alist[:]
        while (i > 0):
            self._percDown(i)
            i = i - 1

class maxHeap(binHeap):
    def __init__(self):
        super().__init__()

    def _percUp(self,i):
        while i // 2 > 0:
          if self._heapList[i] > self._heapList[i // 2]:
             tmp = self._heapList[i // 2]
             self._heapList[i // 2] = self._heapList[i]
             self._heapList[i] = tmp
          i = i // 2

    def _percDown(self,i):
      while (i * 2) <= self._currentSize:
          mc = self._maxChild(i)
          if self._heapList[i] < self._heapList[mc]:
              tmp = self._heapList[i]
              self._heapList[i] = self._heapList[mc]
              self._heapList[mc] = tmp
          i = mc

    def __max__(self):
        return self._heapList([1]) if not self.isEmpty else None

    def _maxChild(self,i):
      if i * 2 + 1 > self._currentSize:
          return i * 2
      else:
          if self._heapList[i*2] > self._heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMax(self):
        retval = self._heapList[1]
        self._heapList[1] = self._heapList[self._currentSize]
        self._currentSize = self._currentSize - 1
        self._heapList.pop()
        self._percDown(1)
        return retval

    def buildHeap(self,alist):
        i = len(alist) // 2
        self._currentSize = len(alist)
        self._heapList = [0] + alist[:]
        while (i > 0):
            self._percDown(i)
            i = i - 1

if __name__ == '__main__':
    h = maxHeap()
    h.buildHeap([10,50,15,30,20,90])
    pq = minHeap()  # Priority Queue using minHeap
    pq.buildHeap([10,50,15,30,20,90])
     


    
