from recursiveFunctions import *

print('iterative fatorial de 5 ',iterativeFactorial(5))
print('recursive fatorial de 5 ',factorial(5))
print('recursive fatorial(1) de 5 ',factorial1(5))

print('MDC entre 6 e 15 : ',MDC(6,15))
print('MMC entre 12 e 30 : ',MMC(12,30))

s = ''
for i in range(5):
     s += str(fibonacci(i))+','
print('Fibonacci 5 termos : ',s[:len(s)-1])
s = ''
for i in range(5,0,-1):
     s += str(tailFibonacci(i,1,1))+','
s = s[:len(s)-1]
print('Fibonacci por cauda de 5 termos : ',s[::-1])

s = ''
for i in range(1,6):
     s += str(fibCassini(i))+','
s = s[:len(s)-1]
print('fibCassini de 5 termos : ',s)
print('soma  3 + 4 = ',soma(3,4))
print('diferença 3 - (-5) = ',diferenca(3,-5))
#print(fibm(6))




