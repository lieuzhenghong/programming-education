import turtle
import math
import time
import sys


# Initialise the three objects

window = turtle.Screen()  # initialise the window
ball = turtle.Turtle()
paddle1 = turtle.Turtle() # do the same for the first paddle
paddle2 = turtle.Turtle() # ... same for the second paddle

window.setworldcoordinates(-400, -400, 400, 400) # set the coordinates of the window

# TODO:
# Move the balls and the paddles to the appropriate locations
# Change the turtle shape of the balls and paddles as they are all arrows right now


#paddle1.tracer(False)
#paddle2.tracer(False)

paddle1.up()
paddle2.up()

paddle1.setpos(-390,-0)
paddle2.setpos(390,-0)

paddle1.shape('square')
paddle1.shapesize(10, 1, 1)
paddle1.color('red')	
paddle2.shape('square')
paddle2.shapesize(10,1,1)
paddle2.color('blue')
ball.shape('circle')
ball.color('green')

window.tracer(False)

velocity = [0.5,0]
p1_energy = 5
p2_energy = 5

def p1_up():
    paddle1.setpos(paddle1.pos()[0], paddle1.pos()[1]+40)
def p1_down():
    paddle1.setpos(paddle1.pos()[0],paddle1.pos()[1]-40)
def p2_up():
    paddle2.setpos(paddle2.pos()[0],paddle2.pos()[1]+40)
def p2_down():
    paddle2.setpos(paddle2.pos()[0],paddle2.pos()[1]-40)
def p1_shrinkpaddle():
    global p1_energy
    if p1_energy >= 1:
        paddle2.shapesize(3,0.5,0.5)
        p1_energy = p1_energy - 1	
        s1.clear()
        s1.goto(0,200)
        s1.write("{} - {}".format(p1_score, p2_score), False, "center", font=("Laksaman", 48, "bold"))
        s1.goto(0,180)
        s1.write("{} : {}".format(p1_energy, p2_energy), False, 'center', font=('Laksaman', 24, 'bold'))                       
def p2_shrinkpaddle():
    global p2_energy
    if p2_energy >= 1:
        paddle1.shapesize(3,0.5,0.5)
        p2_energy = p2_energy - 1
        s1.clear()
        s1.goto(0,200)
        s1.write("{} - {}".format(p1_score, p2_score), False, "center", font=("Laksaman", 48, "bold"))
        s1.goto(0,180)
        s1.write("{} : {}".format(p1_energy, p2_energy), False, 'center', font=('Laksaman', 24, 'bold'))                       
def p1_reverseball():
    global p1_energy
    global velocity
    if p1_energy >= 1:
        p1_energy = p1_energy - 1
        s1.clear()
        s1.goto(0,200)
        s1.write("{} - {}".format(p1_score, p2_score), False, "center", font=("Laksaman", 48, "bold"))
        s1.goto(0,180)
        s1.write("{} : {}".format(p1_energy, p2_energy), False, 'center', font=('Laksaman', 24, 'bold'))                       
        velocity = [velocity[0] * -1, velocity[1] * -1]
                
def p2_reverseball():
    global p2_energy
    global velocity
    if p2_energy >= 1: 
        p2_energy = p2_energy -1
        s1.clear()
        s1.goto(0,200)
        s1.write("{} - {}".format(p1_score, p2_score), False, "center", font=("Laksaman", 48, "bold"))
        s1.goto(0,180)
        s1.write("{} : {}".format(p1_energy, p2_energy), False, 'center', font=('Laksaman', 24, 'bold'))
        velocity = [velocity[0] * -1, velocity[1] * -1]   

        
window.listen() #listen for key being pressed
window.onkey(p1_up, "w")
window.onkey(p1_down,"s")
window.onkey(p2_up, "Up")
window.onkey(p2_down,"Down")
window.onkey(p1_shrinkpaddle, "a")
window.onkey(p2_shrinkpaddle, "Left") 
window.onkey(p1_reverseball, "d")
window.onkey(p2_reverseball, "Right")

p1_score = 0
p2_score = 0

s1 = turtle.Turtle();
s1.up()
s1.goto( 0,200 )
s1.write("{} - {}".format(p1_score, p2_score), False, "center", font=("Laksaman", 48, "bold"))
s1.goto(0, 180)
s1.write("{} : {}".format(p1_energy, p2_energy), False, 'center', font=('Laksaman', 24, 'bold'))
s1.hideturtle()

while True: # whatever in the loop keeps running
    p1_length = paddle1.shapesize()[0] * 15
    p2_length = paddle2.shapesize()[0] * 15
    top1 = paddle1.pos()[1]+ p1_length
    btm1 = paddle1.pos()[1]- p1_length
    top2 = paddle2.pos()[1]+ p2_length
    btm2 = paddle2.pos()[1]- p2_length

    if (ball.pos()[0] <= -400): # left edge of screen 
        ball.setpos(0,0)
        velocity = [-0.5,0]
        paddle1.shapesize(10,1,1)
        paddle2.shapesize(10,1,1)
        paddle1.setpos(-390,-0)
        paddle2.setpos(390,-0)
        time.sleep(1)
        p2_score = p2_score + 1
        print ("{}-{}".format(p1_score, p2_score))
        s1.clear()
        s1.goto(0,200)
        s1.write("{} - {}".format(p1_score, p2_score), False, "center", font=("Laksaman", 48, "bold"))
        s1.goto(0,180)
        s1.write("{} : {}".format(p1_energy, p2_energy), False, 'center', font=('Laksaman', 24, 'bold'))
    elif (ball.pos()[0]>= 400): # right edge of screen 
        ball.setpos(0,0)
        velocity = [0.5,0]
        paddle1.shapesize(10,1,1)
        paddle2.shapesize(10,1,1)
        paddle1.setpos(-390,-0)
        paddle2.setpos(390,-0)
        time.sleep(1)
        p1_score = p1_score + 1
        print ("{}-{}".format(p1_score, p2_score))
        s1.clear()
        s1.goto(0,200)
        s1.write("{} - {}".format(p1_score, p2_score), False, "center", font=("Laksaman", 48, "bold"))
        s1.goto(0,180)
        s1.write("{} : {}".format(p1_energy, p2_energy), False, 'center', font=('Laksaman', 24, 'bold'))
        pass
        velocity = [velocity[0],velocity[1]*-1]
        #do something else
    elif(ball.pos()[1] >= 400): #edge of screen
        velocity = [velocity[0],velocity[1]*-1]
        #do something else
    elif (ball.pos()[1] <= -400):
        velocity = [velocity[0],velocity[1]*-1]
    elif (ball.pos()[0] >= 370 and ball.pos()[1] < top2 and ball.pos()[1] > btm2): # hit collision player 2
        #velocity = [velocity[0]*-1,velocity[1]]
        angle = ((ball.pos()[1] - paddle2.pos()[1])/300.0) * 1.3
        v = math.sqrt(velocity[0]**2 + velocity[1]**2)
        velocity = [-1 * v * math.cos(angle), v * math.sin(angle)]
    elif (ball.pos()[0] <= -370 and ball.pos()[1]< top1 and ball.pos()[1] > btm1): # hit collision player 1
       #velocity = [velocity[0]*-1,velocity[1]]
        angle = ((ball.pos()[1] - paddle1.pos()[1])/300.0) * 1.3
        v = math.sqrt(velocity[0]**2 + velocity[1]**2)
        velocity = [v * math.cos(angle), v * math.sin(angle)]
    else:
        pass
 
    ball.setpos(ball.pos()[0]+velocity[0],ball.pos()[1]+velocity[1])
    ball.up()	
    #print(ball.pos())
    #print(ball.pos()[0])
    #print(ball.pos()[1])
    if(p1_score + p2_score == 11):
        #sys.exit(0)
        p1_score = 0
        p2_score = 0
        p1_energy = 5
        p2_energy = 5
   
    window.update()
    

window.mainloop()

