# adapted  from
# https://runestone.academy/runestone/books/published/pythonds/Trees/ParseTree.html
import operator
from Tree import binaryTree
import sys
sys.path.append('../Collections')
from stack import stack

class parseTree(binaryTree):
     def __init__(self):
          super().__init__()

     def insertSpace(self,exp):
          # função que insere espaços em branco entre os símbolos
          newexp=''
          for ch in exp:
               if ch in ['(',')','+','-','*','/']:                                  
                   newexp += ' ' + ch + ' '
               else:
                    newexp += ch
          return newexp
     
     def buildParseTree(self,exp):
         exp = self.insertSpace(exp)
         #print(exp)
         explist = exp.split()
         st = stack()
         self.insertRoot('')
         st.push(self._root)
         current = self._root
         for ch in explist:
             if ch == '(':
                 self.insertLeft(current,'')
                 st.push(current)
                 current = current.left
             elif ch in ['+', '-', '*', '/']:
                 current.element = ch
                 self.insertRight(current,'')
                 st.push(current)
                 current = current.right
             elif ch == ')':
                 current = st.pop()

             elif ch not in ['+', '-', '*', '/', ')']:
                 try:
                     current.element = ch
                     parent = st.pop()
                     current = parent

                 except ValueError:
                     raise ValueError("token '{}' is not a valid integer".format(i))

         return self

     def __str__(self):
          return str(self._evaluate(self._root))
          
     def eval(self):
          return self._evaluate(self._root)
     
     def _evaluate(self,root):
         opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

         leftC = root.left
         rightC = root.right
         
         if leftC and rightC:
             fn = opers[root.element]
             return fn(self._evaluate(leftC),self._evaluate(rightC))
         else:
             return eval(root.element)
          
if __name__ == '__main__':

     pt = parseTree()
     pt.buildParseTree('(3+(4*5))')
     print(pt.preOrder())
     print(pt.eval())
     
     pt = parseTree()     
     print(eval('((10+5)*3)'))     
     pt.buildParseTree('(((10-5)*3)/(1+3))')
     print(pt.posOrder()) 
     print(pt.inOrder())  
     print(pt.eval())
     print(eval('(((10-5)*3)/(1+3))'))
     
