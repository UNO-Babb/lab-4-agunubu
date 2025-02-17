#TurtleGraphics.py
#Name: Aurora Gunubu
#Date: 2/16/25
#Assignment: Lab 4 - Turtle Graphics

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(ora, sides):
    for s in range(sides):
        ora.forward(50)
        ora.right(360/sides)
    

def fillCorner(sal, corner):
    drawSquare(sal, 100)
    
    if corner == 1:
        sal.begin_fill()
        drawSquare(sal, 50)
        sal.end_fill()
    elif corner == 2:
        sal.forward(50)
        sal.begin_fill()
        drawSquare(sal, 50)
        sal.end_fill()
    elif corner == 3:
        sal.right(90)
        sal.forward(50)
        sal.left(90)
        sal.begin_fill()
        drawSquare(sal, 50)
        sal.end_fill()
        
            
def squaresInSquares(myTurtle, size, numberOfSquares):
    # Centering my square (had to ask a classmate for help on this part)
    myTurtle.penup()
    myTurtle.goto(-size/2, size/2)  # Start at top-left of first square
    myTurtle.pendown()
    
    for i in range(numberOfSquares):
        drawSquare(myTurtle, size)
        myTurtle.penup()
        
        myTurtle.forward(20)
        myTurtle.right(90)
        myTurtle.forward(20)
        myTurtle.left(90)
        
        myTurtle.pendown()
        size-=40
      

        
def main():
    myTurtle = turtle.Turtle()
    
    #drawSquare(myTurtle, 100)
    
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon

    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    #squaresInSquares(myTurtle, 200, 5) #draws 5 concentric squares
    squaresInSquares(myTurtle, 200, 3) #draws 3 concentric squares


main()
