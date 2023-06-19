from stack import stack

def parChecker(symbolString):
    s = stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def symbolChecker(symbolString):
    
    def matches(open,close):    
        opens = "([{"
        closers = ")]}"
        return opens.index(open) == closers.index(close)

    s = stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def decToBin(decNumber):
    rStack = stack()   # reminder stack 
    while decNumber > 0:
        rem = decNumber % 2
        rStack.push(rem)
        decNumber = decNumber // 2

    result = ""
    while not rStack.isEmpty():
        result += str(rStack.pop())

    return result

def decimaltobase(n,base):
    rStack = stack() # reminder stack 
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
        n = n // base  # quotient of dividing n by the base
    result = ""
    while not rStack.isEmpty():
        result += str(rStack.pop())
    return result

if __name__ == '__main__':
    """
    print('parChecker')
    print(parChecker('((()))'))
    print(parChecker('(()'))
    print('symbolChecker')
    print(symbolChecker('{{([][])}()}'))
    print(symbolChecker('[{()]'))
    """
    print('43 in binário ',decToBin(255))
    print('decimal 1453 to base 2 ',decimaltobase(255,2))
    print('decimal 1453 to base 8 ',decimaltobase(1453,8))
    print('decimal 1453 to base 10 ',decimaltobase(1453,10))
    print('decimal 1453 to base 16 ',decimaltobase(1453,16))



        
