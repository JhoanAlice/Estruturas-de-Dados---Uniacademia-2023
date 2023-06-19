from deque import deque

def isPal(aString):
    chardeque = deque()

    for ch in aString:
        chardeque.addRear(ch)

    #stillEqual = True

    while len(chardeque) > 1: # and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            return False #stillEqual = False
    return True

    #return stillEqual


if __name__ == '__main__':
    print('a ',isPal("a"))
    print('radar ',isPal("radario"))



        
