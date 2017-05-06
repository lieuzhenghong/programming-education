import turtle
import math
import time
import sys
import Adafruit_ADS1x15

# Create all objects in the game
###############################
window = turtle.Screen()
# Do not draw the screen automatically
window.tracer(False)

# Create ball and paddles
ball = turtle.Turtle()
paddle1 = turtle.Turtle()
paddle2 = turtle.Turtle()

# Create scoreboard writer
s1 = turtle.Turtle()
s1.up()
s1.goto(0, 200)

# Create analog-digital converter to make the input less complicated
adc = Adafruit_ADS1x15.ADS1015()

# TODO
values = [0, 0]
GAIN = 1
################################

# Set the positions of the screen
# 4 corners: bottom left, top left, bottom right, top right
# Bottom left corner: -400, -400
# Top right corner: 400, 400
# Middle is 0, 0
window.setworldcoordinates(-400, -400, 400, 400)

# Make the paddles not draw a line when moving them
paddle1.up()
paddle2.up()

# Set the positions of the paddles to left edge and right edge
# Paddle 1: left edge
# Paddle 2: right edge
paddle1.setpos(-390, -0)
paddle2.setpos(390, -0)

# Set some properties of the paddles
paddle1.shape('square')
paddle1.shapesize(10, 1, 1)
paddle1.color('red')
paddle2.shape('square')
paddle2.shapesize(10, 1, 1)
paddle2.color('blue')
ball.shape('circle')
ball.color('green')

# Set the speed of the ball:
# The two numbers are x and y
# x = 0.5, y = 0
velocity = [0.5, 0]
# Set energy which is the number of times you can use the powers
p1_energy = 5
p2_energy = 5

# Define two functions which set the y-position of the paddles


def p1_position(y):
    paddle1.setpos(paddle1.pos()[0], y)


def p2_position(y):
    paddle2.setpos(paddle2.pos()[0], y)


def draw_score():
    s1.clear()  # Clear whatever s1 has written
    s1.goto(0, 200)
    # Write the score and energy
    s1.write("{} - {}".format(p1_score, p2_score), False, "center",
             font=("Laksaman", 48, "bold")) s1.goto(0, 180)
    s1.write("{} : {}".format(p1_energy, p2_energy), False, 'center',
             font=('Laksaman', 24, 'bold'))

##################################################
#             POWER UP FUNCTIONS
##################################################
# Two power ups: shrink opponent's paddle & reverse the ball
# Power ups require energy, each player starts with 5 energy


# P1 and P2 shrink paddle functions
def p1_shrinkpaddle():
    global p1_energy  # Get the variable from above
    # Only let the player use powerup if energy is more than 0
    if p1_energy >= 1:
        paddle2.shapesize(3, 0.5, 0.5)  # Shrink the paddle
        p1_energy = p1_energy - 1  # Remove 1 energy
        draw_score()


def p2_shrinkpaddle():
    global p2_energy
    if p2_energy >= 1:
        paddle1.shapesize(3, 0.5, 0.5)
        p2_energy = p2_energy - 1
        draw_score()

# P1 and P2 reverse ball functions
# These functions change the direction of the ball
# Changes both x- and y- direction of the ball


def p1_reverseball():
    global p1_energy
    global velocity
    if p1_energy >= 1:
        p1_energy = p1_energy - 1
        draw_score()


def p2_reverseball():
    global p2_energy
    global velocity
    if p2_energy >= 1:
        p2_energy = p2_energy - 1
        draw_score()

##################################################################


window.listen()  # Start listening for keys being pressed


# When the key is being pressed, call the functions
# When "a" key pressed, shrink the paddle of player 2
window.onkey(p1_shrinkpaddle, "a")
# When "Left" key pressed, shrink the paddle of player 1
window.onkey(p2_shrinkpaddle, "Left")
# When "d" key pressed, reverse the ball of player 2
window.onkey(p1_reverseball, "d")
# When "Right" key pressed, reverse the ball of player 1
window.onkey(p2_reverseball, "Right")

# Score
p1_score = 0
p2_score = 0

# Write the scores and energy of the players
draw_score()


def scale(x):
    return (x - 800)/2.05

###########################################
# START OF WHILE LOOP
###########################################


while True:
    # Length of paddles 1 and 2
    p1_length = paddle1.shapesize()[0] * 15
    p2_length = paddle2.shapesize()[0] * 15
    # Top and bottom of paddles 1 and 2
    top1 = paddle1.pos()[1] + p1_length
    btm1 = paddle1.pos()[1] - p1_length
    top2 = paddle2.pos()[1] + p2_length
    btm2 = paddle2.pos()[1] - p2_length

    # TODO: read the values from the ADC which will correspond to paddle
    # position
    for i in range(2):
        values[i] = adc.read_adc(i, gain=GAIN)
        values[i] = scale(i)

    # Set position of the two paddles
    p1_position(values[0])
    p2_position(values[1])

    ####################################
    # BALL CHECKING ###########
    ####################################
    # Check whether the ball is outside of the screen or when the ball
    # touches a player's paddle
    # If ball is outside of the screen (y-direction)
    # - Bounce off the "wall"
    # If ball is outside of the screen (x-direction)
    # - Award a point to the player opposite the wall
    # - Example: if the ball gets out of the left edge of the screen,
    # -          award the point to player 2.
    # If ball touches a player's paddle
    # - Bounce off the paddle

    # Check whether the ball is outside the left edge of screen
    # If so, then award player 2 one point
    if (ball.pos()[0] <= -400):
        ball.setpos(0, 0)  # Set ball position to center of the screen
        velocity = [-0.5, 0]  # Set ball speed to start value
        # Reset the size of both paddles because the paddles might
        # have shrunk
        paddle1.shapesize(10, 1, 1)
        paddle2.shapesize(10, 1, 1)
        # Reset the position of both paddles to the original position
        paddle1.setpos(-390, -0)
        paddle2.setpos(390, -0)
        # Wait one second to give the player some time to get ready
        time.sleep(1)
        # Award player 2 one point and re-draw the score.
        p2_score = p2_score + 1
        draw_score()

    elif (ball.pos()[0] >= 400):
        ball.setpos(0, 0)
        velocity = [0.5, 0]
        paddle1.shapesize(10, 1, 1)
        paddle2.shapesize(10, 1, 1)
        paddle1.setpos(-390, -0)
        paddle2.setpos(390, -0)
        time.sleep(1)
        p1_score = p1_score + 1
        draw_score()

    ##########

    # If the ball touches the bottom or top of the screen, bounce the ball
    elif(ball.pos()[1] >= 400):
        velocity = [velocity[0], velocity[1]*-1]

    elif (ball.pos()[1] <= -400):
        velocity = [velocity[0], velocity[1]*-1]

    # If the ball touches a paddle, bounce the ball
    # Check 3 things:
    # 1. x-position of ball is more than or equal to the start of the paddle
    # 2. y-position of ball is less than the top of player 2's paddle
    # 3. y-position of ball is more than the bottom of player 2's paddle
    elif (ball.pos()[0] >= 370 and
          ball.pos()[1] < top2 and
          ball.pos()[1] > btm2):
        # TODO: explain the angle
        angle = ((ball.pos()[1] - paddle2.pos()[1])/300.0) * 1.3
        v = math.sqrt(velocity[0]**2 + velocity[1]**2)
        velocity = [-1 * v * math.cos(angle), v * math.sin(angle)]

    elif (ball.pos()[0] <= -370 and
          ball.pos()[1] < top1 and
          ball.pos()[1] > btm1):
        # TODO: explain the angle
        angle = ((ball.pos()[1] - paddle1.pos()[1])/300.0) * 1.3
        v = math.sqrt(velocity[0]**2 + velocity[1]**2)
        velocity = [v * math.cos(angle), v * math.sin(angle)]

    # Otherwise, if ball is not any of the above, do nothing
    else:
        pass

    #########################################

    # Set the position of the ball
    ball.setpos(ball.pos()[0] + velocity[0], ball.pos()[1] + velocity[1])
    ball.up()

    ####################################
    # END GAME
    ####################################
    # If the total score is 11, restart the game.
    if(p1_score + p2_score == 11):
        p1_score = 0
        p2_score = 0
        p1_energy = 5
        p2_energy = 5

    ######################

    window.update()  # Draw the screen

###############################################
# END OF WHILE LOOP
###############################################
window.mainloop()
