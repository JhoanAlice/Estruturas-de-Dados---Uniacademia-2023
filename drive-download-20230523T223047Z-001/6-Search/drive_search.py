# Driver program to test above function 
from search import *
import random
import time

alist = []
print("gerando vetor")
for i in range(1000000):
     alist.append(random.randint(1,5000000))
alist.sort()
start_time = time.time()
key=45950 #alist[1000]
print('Pesquisa chave ',key)
#print('scan')
#print('pos ',scan(alist,key))
elapsed_time = time.time() - start_time
print(elapsed_time, 'seconds')
start_time = time.time()
print('recursive binary search')
print('pos ',recursiveBinarySearch(alist,key))
elapsed_time = time.time() - start_time
print(elapsed_time, 'seconds')

print('iterative interpolation search')
print('pos ',iterativeInterpolationSearch(alist,key))
print('iterative blocked search')
print('pos ',iterativeBlockedSearch(alist,key))
print('blocked binary search')
print('pos',blockedBinarySearch(alist,key))

"""
#key = alist[54031]
#key = 90
#alist = [10,25,30,45,50,55,60,90,100,110,115,120]
#alist = [10,15,20,35,40,45,70,90]
#alist = [10,11,20,25,35,70,71,90,150,200]
#print(alist)
print('Pesquisa chave ',key)
print('scan')
print('pos ',scan(alist,key))

#print('recursive scan')
#print('pos ',recursiveScan(alist,key))

#print('iterative binary search')
#print('pos ',iterativeBinarySearch(alist,key))
print('recursive binary search')
print('pos ',recursiveBinarySearch(alist,key))

#print('iterative interpolation search')
#print('pos ',iterativeInterpolationSearch(alist,key))

#print('iterative blocked search')
#print('pos ',iterativeBlockedSearch(alist,key))
#print('blocked binary search')
#print('pos',blockedBinarySearch(alist,key))



### Pesquisa chave string
alist = []
print("gerando vetor")
for i in range(100000):
     key = ''
     for j in range(15):
          key += chr(random.randint(97,122))
     key = key[:5]+' '+ key[5:10]+' '+ key[10:]
     alist.append(key)
alist.sort()
key = alist[5431]
print(key)
print('pesquisando')
pos=blockedBinarySearch(alist,key)
"""
#print(pos,alist[pos]

elapsed_time = time.time() - start_time
print(elapsed_time, 'seconds')




