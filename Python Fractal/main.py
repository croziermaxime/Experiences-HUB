from turtle import *


def snowflake(length, levels):
    """
    Draws a snowflake of the given length and levels.
    :param length:
    :param levels:
    """
    if levels == 0:
        forward(length)
        return
    length /= 3.0
    snowflake(length, levels - 1)
    left(60)
    snowflake(length, levels - 1)
    right(120)
    snowflake(length, levels - 1)
    left(60)
    snowflake(length, levels - 1)


def create_snowflake(sides, length):
    """
    Draws a snowflake of the given sides and length.
    :param sides:
    :param length:
    """
    colors = ["red", "orange", "yellow", "red", "orange", "yellow"]
    for i in range(sides):
        color(colors[i + 1])
        snowflake(length, sides)
        right(360 / sides)
    pass


def sierpinski(level, size):
    """
    Draws a Sierpinski triangle of the given level and size.
    :param level:
    :param size:
    """
    if level == 0:
        forward(size)
        left(120)
        forward(size)
        left(120)
        forward(size)
        left(120)
    else:
        sierpinski(level - 1, size / 2)
        color("purple")
        forward(size / 2)
        sierpinski(level - 1, size / 2)
        color("pink")
        left(120)
        forward(size / 2)
        right(120)
        sierpinski(level - 1, size / 2)
        color("purple")
        right(120)
        forward(size / 2)
        left(120)


speed(0)
left(90)
width(2)

# sierpinski(5, 300)
create_snowflake(3, 400)

mainloop()
