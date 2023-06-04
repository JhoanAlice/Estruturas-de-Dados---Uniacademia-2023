from stack import stack
from Queue import Queue

def result(F):
    pass

if __name__ == '__main__':
    # expressão infixada 3 + 5 * 8
    # expressão pósfixada 3 5 8 * +
    # resultado 43
    print(result(Queue(['3','5','8','*','+'])))
    # expressão infixada 3 * 5 + 8
    # expressão pósfixada 3 5 * 8 +
    # resultado 23
    print(result(Queue(['3','5','*','8','+'])))
         
        


        
