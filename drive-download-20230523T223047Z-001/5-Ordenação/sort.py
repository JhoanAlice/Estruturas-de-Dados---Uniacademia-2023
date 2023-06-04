
def swap(alist,i,j):
    alist[i],alist[j] = alist[j],alist[i]

def swap2(alist,i,j): # outra versão do swap
    temp = alist[i]
    alist[i] = alist[j]
    alist[j] = temp

def traditionBubbleSort(alist):
  N = len(alist)
  for passnum in range(1, N): 
      for i in range(0,N-passnum):
          if alist[i]>alist[i+1]:
              swap(alist,i,i+1)
  return alist

def bubbleSort(alist):
  N = len(alist)
  for passnum in range(1,N):
      trocou=False
      #print('A')
      for i in range(0,N-passnum):
          if alist[i]>alist[i+1]:
              swap(alist,i,i+1)
              #print('B')
              trocou=True
      if(not trocou):break
  return alist

def selectSort(alist):
  N = len(alist)
  for i in range(0,N-1):
     positionOfMin=i
     #print('A')
     for j in range(i+1,N):
         if alist[j]<alist[positionOfMin]:
             positionOfMin = j
             #print('B')
     swap(alist,i,positionOfMin)
  return alist

def quickSort(alist):
   N = len(alist)
   def recursiveQuickSort(alist,posMin,posMax):
      if(posMin<posMax):
          p=partition(alist,posMin,posMax)
          recursiveQuickSort(alist,posMin,p-1)
          recursiveQuickSort(alist,p+1,posMax)
      return alist  
   def partition(alist,posMin,posMax):
      pivot=alist[posMin]
      i=posMin+1
      j=posMax      
      while True:        
          while(i<posMax and alist[i]<=pivot):
              i=i+1         
          while(j>posMin and alist[j]>=pivot):
              j=j-1
          if(i<j): swap(alist,i,j)
          if(i>=j): break 
      swap(alist,posMin,j)
      return j
    
   return recursiveQuickSort(alist,0,N-1)


def insertSort(alist):
  N = len(alist)
  for i in range(1,N):
    aux=alist[i]
    j=i-1
    #print('A')
    # Achar a posição do menor elemento
    while( j >= 0  and alist[j] >= aux):
        alist[j+1]=alist[j]
        j=j-1
        #print('B')
    alist[j+1]=aux              
  return alist

def shellSort(alist):
    def insertionSort(nlist,start,gap):
      
      for i in range(start+gap,len(nlist),gap):
          current_value = nlist[i]
          position = i
          while position>=gap and nlist[position-gap]>current_value:
              nlist[position]=nlist[position-gap]
              position = position-gap
          nlist[position]=current_value

    sublistcount = len(alist)//2
    while sublistcount > 0:
        for start_position in range(sublistcount):
            insertionSort(alist, start_position, sublistcount)
            #print("After increments of size",sublistcount, "The list is",alist)
        sublistcount = sublistcount // 2
    return alist


     
def merge(alist,mid):
      lefthalf = alist[:mid]
      righthalf = alist[mid:]
      i=j=k=0
      while i < len(lefthalf) and j < len(righthalf):
          if lefthalf[i] <= righthalf[j]:
              alist[k]=lefthalf[i]
              #print('A')
              i += 1
          else:
              alist[k]=righthalf[j]
              j += 1
              #print('B')
          k += 1
      while i < len(lefthalf):
          alist[k]=lefthalf[i]
          #print('C')
          i += 1
          k += 1

      while j < len(righthalf):
          alist[k]=righthalf[j]
          #print('D')
          j += 1
          k +  1
      return(alist)


# Function to merge the two haves alist[0..m] and alist[m..r]
def iterativeMerge(alist,left,mid,right):    
  # create temp arrays 
  L = alist[left:mid]
  R = alist[mid:right] 
  #print(L)
  #print(R)
  # Merge the temp arrays back into alist
  i = 0 
  j = 0 
  k = left 
  while (i < len(L) and j < len(R)): 
      if (L[i] <= R[j]): 
          alist[k] = L[i] 
          i = i + 1
      else:        
          alist[k] = R[j] 
          j = j + 1         
      k = k + 1 

  #* Copy the remaining elements of L[], if there are any */
  while (i < len(L)): 
      alist[k] = L[i] 
      i = i + 1
      k = k + 1  

  while (j < len(R)): 
      alist[k] = R[j] 
      j = j + 1
      k = k + 1  
  return alist

# Iterative mergesort 
def iterativeMergeSort(alist): 
    # curr_size;  For current size of subarrays to be merged 
    #             curr_size varies from 1 to n/2 
    # left_start; For picking starting index of left subarray 
    #             to be merged 
    # Merge subarrays in bottom up manner.  First merge subarrays of 
    # size 1 to create sorted subarrays of size 2, then merge subarrays 
    # of size 2 to create sorted subarrays of size 4, and so on. 
    n = len(alist)
    curr_size = 1
    while curr_size < n:     
        # Pick starting point of different subarrays of current size 
        left_start=0
        while left_start < n:        
            # Find ending point of left subarray. mid+1 is starting  
            # point of right 
            mid = min(left_start + curr_size, n) 
            right_end = min(left_start + 2*curr_size, n)            
            # Merge Subarrays arr[left_start...mid] & arr[mid+1...right_end] 
            iterativeMerge(alist, left_start, mid, right_end)
            left_start += 2*curr_size
        curr_size = 2*curr_size
    return alist


def recursiveMergeSort(alist):
    N = len(alist)
    if len(alist)>1:
        mid = N // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        lefthalf=recursiveMergeSort(lefthalf)
        righthalf=recursiveMergeSort(righthalf)
        alist=merge(lefthalf+righthalf,mid)
    return alist

  
# To heapify subtree rooted at index i. 
# n is size of heap 
def _heapify(arr, n, i): 
    largest = i  # Initialize largest as root 
    left = 2 * i + 1     # left = 2*i + 1 
    right = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if left < n and arr[i] < arr[left]: 
        largest = left 
  
    # See if right child of root exists and is 
    # greater than root 
    if right < n and arr[largest] < arr[right]: 
        largest = right 
  
    # Change root, if needed 
    if largest != i: 
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        # Heapify the root.
        _heapify(arr, n, largest)
 
# The main function to sort an array of given size 
def heapSort(arr):
    # https://www.programiz.com/dsa/heap-sort
    n = len(arr) 
  
    # Build a maxheap. 
    # Since last parent will be at ((n//2)-1) we can start at that location. 
    for i in range(n // 2 - 1, -1, -1): 
        _heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # swap 
        _heapify(arr, i, 0) 

# Method to do Radix Sort
def radixSort(arr):

    # Python program for implementation of Radix Sort    
    # A function to do counting sort of arr[] according to 
    # the digit represented by exp. 
    def countingSort(arr, exp1): 
     
          n = len(arr) 
         
          # The output array elements that will have sorted arr 
          output = [0] * (n) 
         
          # initialize count array as 0 
          count = [0] * (10) 
         
          # Store count of occurrences in count[] 
          for i in range(0, n): 
              index = (arr[i]/exp1) 
              count[int((index)%10)] += 1
         
          # Change count[i] so that count[i] now contains actual 
          #  position of this digit in output array 
          for i in range(1,10): 
              count[i] += count[i-1] 
         
          # Build the output array 
          i = n-1
          while i>=0: 
              index = (arr[i]/exp1) 
              output[ count[ int((index)%10) ] - 1] = arr[i] 
              count[int((index)%10)] -= 1
              i -= 1
         
          # Copying the output array to arr[], 
          # so that arr now contains sorted numbers 
          i = 0
          for i in range(0,len(arr)): 
              arr[i] = output[i]

    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1/exp > 0:
          countingSort(arr,exp)
          exp *= 10
    return arr

# bubbleSort walking inverse ( end to front )
def bubbleSort1(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                swap(alist,i,i+1)
    return alist

# select sort walking inverse ( end to front )  choice max
def selectSort1(alist):
  for i in range(len(alist)-1,0,-1):
     positionOfMax=0
     for location in range(1,i+1):
         if alist[location]>alist[positionOfMax]:
             positionOfMax = location
     swap(alist,i,positionOfMax);
  return alist

# insert walking inverse ( end to front )
def insertSort1(alist):
  N = len(alist)
  for i in range(N-2,-1,-1):
    aux=alist[i]
    j=i+1
    # Achar a posição do menor elemento
    while(j <= N-1 and alist[j]<=aux):
        alist[j-1]=alist[j]
        j=j+1         
    alist[j-1]=aux              
  return alist

  
      
