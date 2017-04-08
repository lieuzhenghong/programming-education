from turtle import *
window = Screen()
ball = Turtle() #create a turtle called ball
p1 =  Turtle() # do the same for the first paddle
p2 = Turtle()# same here
 
window.setworldcoordinates(-400, -400, 400, 400) # define the size of the window
window.tracer(False)
# TODO
# Now we have created the three turtles.
# 1. Move the turtles into the correct position.
# 2. change the shapes of the turtle. use turtle.shape('circle')
#   and turtle.shape('square') for example
p1.up()
p2.up()
ball.up()
p1.setpos(0,350)
p2.setpos(0,-350)
p1.right(90)
p2.left(90)
 
p1.shape('square')
p1.shapesize(7, 1)
p2.shape('square')
p2.shapesize(7, 1)
ball.shape('circle')
ball.shapesize(1, 1)
 
# We have successfully initialised the positions of the ball and paddles.
# Now, we need to make the keys control the paddles.
def p1_left():
    # Change from 0, 350 --> -10, 350
    # p1.pos()  --> [30, 240] for example
    # p1.pos()[0] --> 30
    # p1.pos()[1] --> 240
    x = p1.pos()[0]
    y = p1.pos()[1]
    print(x)
    # Change the position
    if p1.pos()[0]<= -310:
        pass
    else:
        p1.setpos(x-10,y)
 
 
def p1_right():
    x = p1.pos()[0]
    y = p1.pos()[1]
    print(x)
    if p1.pos()[0]>= 310:
        pass
    else:
        p1.setpos(x+10,y)
 
def p2_left():
    x = p2.pos()[0]
    y = p2.pos()[1]
    print(x)
    if p2.pos()[0]<= -310:
        pass
    else:
        p2.setpos(x-10,y)
 
def p2_right():
    x = p2.pos()[0]
    y = p2.pos()[1]
    print(x)
    if p2.pos()[0]>= 310:
        pass
    else:
        p2.setpos(x+10,y)

v = [0, 1]
 
def move_ball():
    global v
    ball.setpos(ball.pos()[0] +  v[0] , ball.pos()[1] + v[1])
    print(ball.pos())
    if (ball.pos()[1] > 400):
        v = [v[0] * -1, v[1] * -1]
        if ball.pos[1]>= 290:
            print(stop)
        else:
            print('continue')
        
window.listen() #listen for key being pressed
window.onkey(p1_left, "Left") #On "Left" being pressed, call the function p1_left
window.onkey(p1_right, "Right")
window.onkey(p2_left, "a")
window.onkey(p2_right, "d")

while True:
    print('test')
    move_ball()
    window.update()
window.mainloop()
