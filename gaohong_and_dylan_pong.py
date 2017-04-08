from turtle import *
import time
window = Screen()
ball = Turtle() #create a turtle called ball
p1 =  Turtle() # do the same for the first paddle
p2 = Turtle()# same here

s1 = Turtle()

 
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


p1_scores = 0
p2_scores = 0 

p1_energy = 0
p2_energy = 0
s1.setpos(0,0)
s1.hideturtle()
s1.write("{}-{}".format(p1_scores,p2_scores),False,font=("Arial",36))
# We have successfully initialised the positions of the ball and paddles.
# Now, we need to make the keys control the paddles.
def p1_left():
    # Change from 0, 350 --> -10, 350
    # p1.pos()  --> [30, 240] for example
    # p1.pos()[0] --> 30
    # p1.pos()[1] --> 240
    x = p1.pos()[0]
    y = p1.pos()[1]
    #print(x)
    # Change the position
    if p1.pos()[0]<= -330:
        pass
    else:
        p1.setpos(x-20,y)
 
 
def p1_right():
    x = p1.pos()[0]
    y = p1.pos()[1]
  
    if p1.pos()[0]>= 330:
        pass
    else:
        p1.setpos(x+20,y)
 
def p2_left():
    x = p2.pos()[0]
    y = p2.pos()[1]
    #print(x)
    if p2.pos()[0]<= -330:
        pass
    else:
        p2.setpos(x-20,y)
 
def p2_right():
    x = p2.pos()[0]
    y = p2.pos()[1]
    #print(x)
    if p2.pos()[0]>= 330:
        pass
    else:
        p2.setpos(x+20,y)

v = [0.25, 0.15]
 
def move_ball():

    global v
    global p1_scores
    global p2_scores
    global p1_energy
    global p2_energy

    ball.setpos(ball.pos()[0] +  v[0] , ball.pos()[1] + v[1])
  
    x = ball.pos()[0]
    y = ball.pos()[1]
    # Paddle 1
    if ball.pos()[1] > 325 and ball.pos()[1]<335 and ball.pos()[0] > p1.pos()[0] - 80 and ball.pos()[0] < p1.pos()[0] + 80:
        v = [v[0], v[1] * -1]
        ball.setpos(x,325)
        p1_energy += 1
        if v[0] > 0:
            v[0] += 0.01
        else:
            v[0] += -0.01
        if v[1]> 0:
            v[1] += 0.01
        else:
            v[1] += -0.01
    
    # Paddle 2
    if ball.pos()[1] < -325 and ball.pos()[1] > -335 and ball.pos()[0] > p2.pos()[0] - 80 and ball.pos()[0] < p2.pos()[0] + 80:
        v = [v[0], v[1] * -1]
        ball.setpos(x,-325)
        p2_energy += 1
        if v[0] > 0:
            v[0] += 0.01
        else:
            v[0] += -0.01
        if v[1] > 0:
            v[1] += 0.01
        else:
            v[1] += -0.01

    #bouncing off y-edge (Scoring)
    if (ball.pos()[1] > 400):
        #v = [v[0], v[1] * -1]
        p2_scores += 1
        ball.setpos(0,0)
        s1.clear()
        s1.write("{}-{}".format(p1_scores,p2_scores),False,font=("Arial",36))
        time.sleep(1)

    if (ball.pos()[1] < -400):
        # bounce the ball
        #v = [v[0], v[1] * -1]
        p1_scores += 1
        ball.setpos(0,0)
        s1.clear()
        s1.write("{}-{}".format(p1_scores,p2_scores),False,font=("Arial",36))
        time.sleep(1)

    #checking x edge
    if (ball.pos()[0] > 400):
        v = [v[0] * -1 , v[1]]
    if (ball.pos()[0] < -400):
        v = [v[0] * -1, v[1]]

def p1_powerup():
    print ('p1 power up used')
def p2_powerup():   
    print ('p2 power up used')

window.listen() #listen for key being pressed
window.onkey(p1_left, "Left") #On "Left" being pressed, call the function p1_left
window.onkey(p1_right, "Right")
window.onkey(p2_left, "a")
window.onkey(p2_right, "d")
window.onkey(p1_powerup,"f")
window.onkey(p2_powerup,"l")


while True:
    move_ball()

    window.update()
window.mainloop()
