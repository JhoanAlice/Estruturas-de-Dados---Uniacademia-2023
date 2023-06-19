# Driver program to test above function 
from sort import *
import random
import time
"""
#alist=[15,20,35,55,21,30,45,50,57,80,81,88,90]
#bubbleSort(alist)
#selectSort(alist)
#insertSort(alist)
print("Merge")
merge(alist,4)

"""
#alist = []
#print("gerando vetor")
#for i in range(10000):
#     alist.append(random.randint(1,5000000))

#start_time = time.time()

#print("start Pyhton Sort ")
#alist.sort()


#traditionBubbleSort(alist)
#print("start BubbleSort")
#bubbleSort(alist)


#print("start SelectSort")
#selectSort(alist)

#print("start InsertSort")
#insertSort(alist)

print("Métodos Eficientes")

#print("start QuickSort")
#quickSort(alist)

#print("start ShelSort")
#shellSort(alist)

#print("start RecursiveMergeSort")
#recursiveMergeSort(alist)

#print("start IterativeMergeSort")
#iterativeMergeSort(alist)

#print("start HeapSort")
#heapSort(alist)

#print("start radixSort")
#radixSort(alist)

#elapsed_time = time.time() - start_time
#print(elapsed_time, 'seconds')

print("gerando vetor do Merge")
arr1 = []
arr2 = []
for i in range(500000):
     arr1.append(random.randint(1,10000))
     arr2.append(random.randint(1,10000))

arr = quickSort(arr1)+quickSort(arr2)
mid = len(arr1)

start_time = time.time()

#arr = [ 17, 26, 44, 54, 20, 31, 55, 77, 85]
#print(arr)
print("Merge")
#merge(arr,mid)
#print(arr)
iterativeMerge(arr,0,mid,len(arr))

elapsed_time = time.time() - start_time
print(elapsed_time, 'seconds')

#

#merge(v,3))
#interativeMerge(v,0,3,9))





