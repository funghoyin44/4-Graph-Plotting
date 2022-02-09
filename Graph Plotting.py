import turtle

#Setting
precision = 200
grid_colour = "grey"
speed = 0
Tracer = True

#Main Functions
def initializing_turtle():
    turtle.title("Graph Plotting Termnal")
    turtle.setworldcoordinates(0, 0, 1000, 1000)
    turtle.speed(speed)

def drawing_grid(precision):
    turtle.tracer(Tracer)
    turtle.pencolor(grid_colour)
    turtle.up()
    #Drawing Horizontal Line
    for i in range(int(1000/ precision)):
        turtle.goto(-precision, precision * i)
        turtle.down()
        turtle.forward(1000 + precision)
        turtle.write(turtle.ycor())
        turtle.up()
    turtle.setheading(90)
    turtle.up()
    #Drawing Vetical Line
    for i in range(int(1000/ precision)):
        turtle.goto(precision * i, -precision)
        turtle.down()
        turtle.forward(1000 + precision)
        turtle.write(turtle.xcor())
        turtle.up()
    turtle.tracer(True)

initializing_turtle()
drawing_grid(precision)
turtle.done()
