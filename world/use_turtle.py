import turtle

def use_turtle():
    screen = turtle.getscreen()
    screen.setup(width=480, height=768)

    turtle_robot = turtle.Turtle()
    turtle_robot.shape('turtle')
    turtle_robot.setheading(90)

    constrained_turtle = turtle.Turtle()
    constrained_turtle.hideturtle()
    constrained_turtle.penup()
    constrained_turtle.setheading(90)
    constrained_turtle.forward(200)
    constrained_turtle.right(90)
    constrained_turtle.forward(100)
    constrained_turtle.pendown()
    constrained_turtle.pencolor('red')

    for i in range(2):
        constrained_turtle.right(90)
        constrained_turtle.forward(400)
        constrained_turtle.right(90)
        constrained_turtle.forward(200)

    return turtle_robot