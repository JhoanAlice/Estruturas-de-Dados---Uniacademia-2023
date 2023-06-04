from turtle import *
#import turtle 
def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

def midlle_point(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(P1,P2,P3,degree,myTurtle):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    if degree == 0:
        drawTriangle([P1,P2,P3],colormap[0],myTurtle)
    else:
        P4 = midlle_point(P1,P2)
        P5 = midlle_point(P2,P3)
        P6 = midlle_point(P1,P3)           
        sierpinski(P1,P4,P6,degree-1, myTurtle)
        sierpinski(P4,P2,P5,degree-1, myTurtle)
        sierpinski(P6,P5,P3,degree-1, myTurtle)
        
def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   P1 = [-100,-50]
   P2 = [0,100]
   P3 = [100,-50]
   sierpinski(P1, P2, P3,4,myTurtle)
   myWin.exitonclick()

main()
