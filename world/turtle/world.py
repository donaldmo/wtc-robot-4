import turtle

screen = turtle.getscreen()
screen.setup(width=480, height=768)

turtle_robot = turtle.Turtle()
turtle_robot.shape('turtle')
turtle_robot.setheading(90)

direction = 1
position = (0, 0)

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

        steps = int(args[1])
        turtle_robot.forward(steps)
        print(f' > {name} moved forward by {steps} steps.')

    # Print the current direction
    print(f'Current Direction: {direction}')
