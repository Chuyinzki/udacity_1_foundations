import turtle


def draw_square(joey):
    for x in range(0, 4):
        joey.forward(100)
        joey.right(90)


def draw_circle_square():
    window = turtle.Screen()
    window.bgcolor("red")
    joey = turtle.Turtle()
    joey.speed(100)

    granularity = 10
    times = 360/granularity

    for x in range(1, times):
        joey.right(granularity)
        draw_square(joey)

    window.exitonclick()


draw_circle_square()
