import turtle
import time
from urllib.request import urlopen
from PIL import Image

# Function to download and save the image locally
def download_image(url, filename):
    with urlopen(url) as response, open(filename, 'wb') as out_file:
        out_file.write(response.read())

# Download the image
image_url = "https://cdna.artstation.com/p/assets/images/images/008/995/196/large/shane-smith-tortoise-character-illustration.jpg?1516554270"
image_filename = "tortoise_image.jpg"
download_image(image_url, image_filename)

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(width=480, height=768)

# Set the background image
screen.bgpic(image_filename)

# Display the image for 5 seconds
time.sleep(5)

# Clear the screen and reset the background
screen.clear()
screen.bgcolor("white")  # Change the background color if needed

# Continue with the rest of your turtle program...

turtle_robot = turtle.Turtle()
turtle_robot.shape('turtle')
turtle_robot.setheading(90)
direction = 1

# Draw a box around the turtle screen
constraint_turtle = turtle.Turtle()
constraint_turtle.hideturtle()
constraint_turtle.penup()
constraint_turtle.goto(-240, 384)  # Starting position for the box
constraint_turtle.pendown()
constraint_turtle.pencolor('red')

for _ in range(2):
    constraint_turtle.forward(480)  # Width of the box
    constraint_turtle.right(90)
    constraint_turtle.forward(768)  # Height of the box
    constraint_turtle.right(90)

# Set up the progress turtle
progress_turtle = turtle.Turtle()
progress_turtle.hideturtle()
progress_turtle.penup()
progress_turtle.goto(0, -screen.window_height() // 2 + 20)  # Adjust the y-coordinate as needed
progress_turtle.pendown()
progress_turtle.pencolor('black')

def update_progress(progress):
    progress_turtle.clear()
    progress_turtle.write(f'Loading... ({progress}%)', align='center', font=('Arial', 16, 'normal'))

name = input('What do you want to name your robot? ')

while True:
    command = input(f'{name}: What must I do next? ').strip()

    if command == 'off':
        screen.bye()
        break

    if command == 'right':
        turtle_robot.right(90)
        direction = (direction % 4) + 1

    if command == 'left':
        turtle_robot.left(90)
        direction = (direction - 2) % 4 + 1

    if command.startswith('forward'):
        args = command.split(' ')

        if not (len(args) >= 2 and args[1].isdigit()):
            print(f'{name}, Sorry, I did not understand {command}.')
            continue

        distance = int(args[1])
        turtle_robot.forward(distance)

        # Update the progress display after each movement
        progress_percent = (turtle_robot.distance(0, 0) / 480) * 100  # Adjust as needed based on your constraints
        update_progress(int(progress_percent))
        
        # Introduce a 2-second timeout
        time.sleep(2)
