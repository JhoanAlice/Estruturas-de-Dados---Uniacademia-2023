def iterativeFactorial(n):
     fat = 1
     for i in range(n,0,-1):
          fat = fat*i
     return fat

def factorial(n):
      return n*factorial(n-1) if n > 0 else 1

def factorial1(n):
     if n == 0:
          return 1
     else:
          return n*factorial1(n-1)

def MMC(x,y):
     return (x*y)/MDC(x,y)

def MDC(x,y):
     if (x == y):
          return x
     elif x < y:
          return MDC(y,x)
     else:
          return MDC(x-y,y)

def fibonacci(n):
     if( n <= 1 ):
          return 1
     else:
          return fibonacci(n-1) + fibonacci(n-2)

def tailFactorial(n):
     def accumulatedFactorial(n,f):
          if ( n == 0):
               return f
          else:
               return accumulatedFactorial(n-1, n*f)
     return accumulatedFactorial(n, 1)

def tailFibonacci(n,current,next):
     if( n == 1):
          return current
     else:
          return tailFibonacci(n-1,next,current+next)

def fibm(n,xi,xii):
     n-=1
     memo = {0:xi, 1:xii}
     def ffibm(n):
         if not n in memo:
             memo[n] = ffibm(n-1) + ffibm(n-2)
         print(memo)
         return memo[n]

     return ffibm(n)

def fibCassini(n):
     if (n == 0):
          return 0 #  base case
     if (n == 1):
          return 1 #  base case
     if (n == 2):
          return 1 #  base case
     if (n % 2 != 0):
          # n is odd
          a = fibCassini((n+1)/2)
          b = fibCassini((n-1)/2)
          return a*a + b*b
     else:
          # n is even
          a = fibCassini(n/2+1)
          b = fibCassini(n/2 - 1)
          return a*a - b*b
     
def sucessor(x):
     return x + 1 

def antecessor(x):
     return x - 1

def soma(a,b):
     if b == 0:
          return a
     elif b > a:
          return soma(b,a)
     return soma(sucessor(a),antecessor(b))
    
def diferenca(a,b):
     if a == b:
          return 0
     elif a < b:
          return (-1)*diferenca(b,a) 
     else:
          return diferenca(antecessor(a),b)+1

def even(n):  # par
     if n == 0:
          return True
     elif n > 0:
          return odd(n-1)
     else:
          return even(-n)

def odd(n):  # impar
     if n == 0:
          return False
     elif n > 0:
          return even(n-1)
     else:
          return odd(-n)

def mystery(n):  
     if n == 0:
          return 1
     else:
          d = n% 10
          return d * mystery(n // 10)

def F(n):  
     if n < 4:
          return  3 * N
     else:
          return 2 * F(n - 4) + 5


     
