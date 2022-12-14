# Turtle lib doc: https://docs.python.org/3/library/turtle.html

# First, make sure you understand the question.
# Second, develop a design/plan of the solution
# In the design, the program is divided into mutiple subtasks
# each subtask is small and clear to program.

# when you start coding, it is very very very important
# to develop the program incrementally, one small subtask/piece at time
# only when the current works correctly, then you move to the next subtask

# in Exam, if you program doesn't compile (has syntax error), you get no more than 20%
# of the score.

# 1. Setup the screen
# 2. draw the target
# 3. ask user to input two parameters: angle and distance
# 4. launch the projectile with the specified angle and distance
# 5. check whethere we hit the target or not, display the hit/miss message


# Hit the Target Game
import turtle
import math

# Named constants

TARGET_LLEFT_X = 200  # Target's lower-left X
TARGET_LLEFT_Y = 300  # Target's lower-left Y
TARGET_WIDTH = 40     # Width of the target

PROJECTILE_SPEED = 1  # Projectile's animation speed

EAST = 0              # Angle of east direction
NORTH = 90            # Angle of north direction
SOUTH = 270           # Angle of south direction
WEST = 180            # Angle of west direction

# Draw the target.
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

# Center the turtle.
turtle.home()
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# Get the angle and force from the user.
width = turtle.window_width()
height = turtle.window_height()
max_distance = int(math.sqrt(width ** 2 + height ** 2) / 2)
distance = int(input(f'Enter the launch distance (1-{max_distance}): '))
angle = int(input("Enter the projectile's angle 0-360: "))

# Set the heading.
turtle.setheading(angle)

# Launch the projectile.
turtle.pendown()
turtle.forward(distance)

xcor = turtle.xcor()
ycor = turtle.ycor()

# Did it hit the target?
is_in_x = ((xcor >= TARGET_LLEFT_X) and
           (xcor <= (TARGET_LLEFT_X + TARGET_WIDTH)))
is_in_y = ((ycor >= TARGET_LLEFT_Y) and
           (ycor <= (TARGET_LLEFT_Y + TARGET_WIDTH)))
is_hit = is_in_x and is_in_y

# show message
if is_hit:
    print('Target hit!')
else:
    print('You missed the target.')

# this keeps the window open
turtle.done()
