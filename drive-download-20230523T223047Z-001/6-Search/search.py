import math

global NOT_FOUND
NOT_FOUND=-1

# iterative scan search
def scan(alist,key):
  N = len(alist)
  for i in range(0, N):
      #print(i)
      if key == alist[i]:
        return i
      elif key < alist[i]:
        return NOT_FOUND        
  return NOT_FOUND

# recursive scanner search
def recursiveScan1(alist,key):
  def bodyRecursiveScan1(alist,key,i):
    N = len(alist)  
    if i == N:
      return NOT_FOUND        
    elif key == alist[i]:
      return i
    elif key < alist[i]:
      return NOT_FOUND        
    return bodyRecursiveScan1(alist,key,i+1)

  return bodyRecursiveScan1(alist,key,0)


# recursive scanner search - another way
def recursiveScan(alist,key):
  def bodyRecursiveScan(alist,key,i):
    N = len(alist)
    if i == N:
      return NOT_FOUND        
    elif key == alist[i]:
      return i
    elif key < alist[i]:
      return NOT_FOUND        
    return bodyRecursiveScan(alist,key,i+1)
  return bodyRecursiveScan(alist,key,0)


# iterative binary search
def iterativeBinarySearch(alist,key):
  N = len(alist)  
  low = 0
  high = N-1
  mid=(low+high) //2
  while(low <= high):
    print(mid)      
    if key == alist[mid]:
      return mid
    elif key < alist[mid]:
      high=mid-1
    else:
      low=mid+1
    mid=(low+high) //2
  return NOT_FOUND

# recursive binary search
def recursiveBinarySearch(alist,key):
    return bodyRecursiveBinarySearch(alist,key,0,len(alist)-1)

def bodyRecursiveBinarySearch(alist,key,low,high):
    mid=(low+high) //2
    print(mid)      
    if low > high:
      return NOT_FOUND    
    if key == alist[mid]:
      return mid
    elif key < alist[mid]:
      return bodyRecursiveBinarySearch(alist,key,low,mid-1)
    else:
      return bodyRecursiveBinarySearch(alist,key,mid+1,high)
    return NOT_FOUND
  
#
# Esta função só vale para chaves numéricas
#  
# interative interpolation search
def iterativeInterpolationSearch(alist,key):
    N = len(alist)
    low=0
    high=N-1
    while(low <= high):
        min = alist[low]
        max = alist[high]
        mid = ( low + abs((high-low ) * (key-min))// (max-min))

        print(mid)      
    
        if(max==min):
          return NOT_FOUND
        if(mid>high or mid<low):
          return NOT_FOUND
        if( alist[ mid ]== key ):
          return mid
        elif( alist[ mid ] < key ):
          low= mid + 1
        else : 
          high=mid - 1
    return NOT_FOUND

#
# Esta função só vale para chaves numéricas
#
# recursive interpolation search
def recursiveInterpolationSearch(alist,key):
  def bodyRecursiveInterpolationSearch(alist,key,low,high):
    if(low<=high):
        min = alist[low]
        max = alist[high]
        mid = ( low + abs((high-low ) * (key-min))// (max-min))
        print(mid)      
        if(max==min):
          return NOT_FOUND
        if(mid>high or mid<low):
          return NOT_FOUND
        if( alist[ mid ] == key ):
          return mid
        if( alist[ mid ] < key ):
          return bodyRecursiveInterpolationSearch(alist,key,mid+1,high)
        else : 
          return bodyRecursiveInterpolationSearch(alist,key,low,mid-1)
    return NOT_FOUND
  
  return bodyRecursiveInterpolationSearch(alist,key,0,len(alist)-1)

def blockScan(key,alist,min,max):
    for i in range(min,max):
      print(i)
      
      if key == alist[i]:
        return i
      if key < alist[i]:
        return NOT_FOUND
    return NOT_FOUND
    
# iterative blocked search
def iterativeBlockedSearch(alist,key): 
  N = len(alist)
  block_size= int(math.sqrt(N))  # tamanho lógico do bloco
  for bn in range(0,N // block_size + 1):  # pesquisa do bloco 
    # bn : número do bloco: 0,1,2, ....   
    # inicializa i com o índice da primeira célula do bloco 
    i=block_size*(bn+1)-1 
    if(i >= N): # verifica se índice é maior índice da última célula
      i = N - 1 # retorna i para a posição final do vetor
    print(i, bn)
    if key > alist[i]: # chave maior que a última chave do bloco 
        if i == N - 1 :
          return NOT_FOUND
        else:
          continue
    else:
        # percorre o bloco que pode conter a chave                
        return blockScan(key,alist,bn*block_size,i+1)
  return NOT_FOUND                                                          

def blockedBinarySearch(arr, key): 
    # recursive bodyblockedBinarySearch     
    def bodyBlockedBinarySearch(alist, block_size, low, high, key): 
        mid=(low+high) // 2
        print('bl ',mid)
        if low > high:
            return NOT_FOUND    
        if key < alist[block_size*mid]:
            return bodyBlockedBinarySearch(alist,block_size,low,mid-1,key)
        elif key > alist[block_size*(mid+1)-1]:
            return bodyBlockedBinarySearch(alist,block_size,mid+1,high,key)    
        else:
            pos = bodyRecursiveBinarySearch(alist,key,block_size*mid,block_size*(mid+1))
            if pos == -1:
                return NOT_FOUND
            else:
                return pos # pos+block_size*mid
        return NOT_FOUND  
    block_size= int(math.sqrt(len(arr)))   # tamanho lógico do bloco
    return bodyBlockedBinarySearch(arr,block_size,0, len(arr) // block_size, key)


     


  
    
