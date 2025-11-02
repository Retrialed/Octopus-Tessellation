import turtle
from math import sin, cos, radians, sqrt
from time import sleep
from random import randint
#default values (will be dynamically edited if special effects is true)
angle = -120
scale = 60
x_offset = 0
y_offset = 0

#options
special_effects = 0 #switch between 1 and 0 to enable/disable the effects/motion
want_face = 1 #it is very sad that this slows down special effects by so much
draw = 0 #determines if the lines of each piece is shown
width = 12 #adjusts tessellation size (laggy to increase)

def rotate(x, y, r):
    r = radians(r)
    return x * cos(r) - y * sin(r), x * sin(r) + y * cos(r)

reds = [
    "#743B93", "#7B3DB4", "#9E60C4",
    "#B66BBB", "#A04BA5", "#7E1D84",
    "#D470B8", "#CC4CA5", "#AC1B85"
]

greens = [
    "#E976B6", "#EA55A5", "#D22083",
    "#EA749C", "#E95388", "#CF1F66",
    "#E47485", "#E3546B", "#C82346"
]

yellows = [
    "#DE746C", "#DC554C", "#C42A25",
    "#DD7753", "#DE5B35", "#C32F1F",
    "#EB945B", "#E67840", "#C64D19"
]

blues = [
    "#EEB65C", "#EEA840", "#DF872E",
    "#EAD364", "#ECCC48", "#DEB82C",
    "#E9E177", "#E7E15D", "#DDD544"
]

def hexagon_centers(thickness):
    centers = []
    for row in range(-thickness + 1, thickness):
        start_col = max(-thickness + 1, -row - thickness + 1)
        end_col = min(thickness - 1, -row + thickness - 1)
        for col in range(start_col, end_col + 1):
            x = sqrt(3) * col + sqrt(3) / 2 * row
            y = 3 / 2 * row
            d = (sqrt(x ** 2 + y ** 2) - .25) % 4
            if col == 0 and row == 0:
                color = "#BF3CC1"
            elif d < .9 or (col == 0 and row == 1) or (col == -1 and row == 0) or (col == 1 and row == -1):
                color = reds[randint(0,8)] #red
            elif d < 1.7:
                color = greens[randint(0,8)] #green
            elif d < 3:
                color = yellows[randint(0,8)] #yellow
            else:
                color = blues[randint(0,8)] #blue
            centers.append([x, y, color])
    return centers

def create_pattern(t):
    for xy in hexagon_centers(width):
        t.pu()
        nx, ny = rotate(xy[0], xy[1], angle)
        t.goto(nx * scale + x_offset, ny * scale + y_offset)
        t.fillcolor(xy[2])
        t.begin_fill()
        hexagon(t)
        t.end_fill()
        t.goto(nx * scale + x_offset, ny * scale + y_offset)
        if want_face: face(t)
        t.goto(nx * scale + x_offset, ny * scale + y_offset)
    
def face(t):
    t.lt(120)
    t.dot()
    
    #counterclockwise eye
    t.rt(22.5)
    t.bk(scale / 10)
    t.lt(90)
    t.pd()
    t.fillcolor("white")
    t.begin_fill()
    t.circle(scale / 10, 360)
    t.end_fill()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(scale / 15, 360)
    t.end_fill()
    t.pu()
    t.rt(90)
    t.fd(scale / 10)
    t.lt(22.5)
    
    #clockwise eye
    t.rt(157.5)
    t.bk(scale / 10)
    t.lt(90)
    t.pd()
    t.fillcolor("white")
    t.begin_fill()
    t.circle(scale / 10, 360)
    t.end_fill()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(scale / 15, 360)
    t.end_fill()
    t.pu()
    t.rt(90)
    t.fd(scale / 10)
    t.lt(157.5)
    
    #head
    t.bk(scale / 3)
    t.pd()
    t.rt(90)
    t.fd(scale / 8)
    t.bk(scale / 8)
    t.circle(scale / 3, -180)
    t.bk(scale / 8 + 1)
    t.fd(scale / 8 + 1)
    t.pu()

def hexagon(t):
    t.setheading(0)
    t.lt(angle)
    t.lt(30)
    t.fd(scale)
    t.rt(30)
    if draw: t.pd()
    for _ in range(6):
        side(t.xcor(), t.ycor(), t)
        t.rt(60)
    t.pu()

def side(ox, oy, t):
    for xy in directions:
        newx, newy = rotate(scale * xy[0] / 100, scale * xy[1] * sqrt(3) / 200, t.heading() - 90)
        t.goto(newx + ox, newy + oy)

directions = [[0.0, 0.0], [20.0, 16.8], [30.0, 23.2], [39.0, 31.2], [44.0, 39.2], [46.0, 47.2], [46.0, 52.0], [51.0, 42.4], [52.0, 30.4], [49.0, 24.0], [43.0, 18.4], [37.0, 14.4], [33.0, 11.2], [25.0, 0.0], [25.0, 0.0], [23.0, -2.4], [19.0, -4.8], [18.0, -8.8], [17.0, -16.0], [14.0, -22.4], [14.0, -28.8], [15.0, -35.2], [18.0, -42.4], [22.0, -47.2], [29.0, -51.2], [33.0, -56.8], [35.0, -51.2], [31.0, -44.8], [27.0, -38.4], [25.0, -32.8], [25.0, -27.2], [27.0, -19.2], [30.0, -13.6], [34.0, -8.8], [40.0, -4.0], [50.0, 0.0], [50.0, 0.0], [60.0, 4.0], [66.0, 8.8], [70.0, 13.6], [73.0, 19.2], [75.0, 27.2], [75.0, 32.8], [73.0, 38.4], [69.0, 44.8], [65.0, 51.2], [67.0, 56.8], [71.0, 51.2], [78.0, 47.2], [82.0, 42.4], [85.0, 35.2], [86.0, 28.8], [86.0, 22.4], [83.0, 16.0], [82.0, 8.8], [81.0, 4.8], [77.0, 2.4], [75.0, 0.0], [75.0, 0.0], [67.0, -11.2], [63.0, -14.4], [57.0, -18.4], [51.0, -24.0], [48.0, -30.4], [49.0, -42.4], [54.0, -52.0], [54.0, -47.2], [56.0, -39.2], [61.0, -31.2], [70.0, -23.2], [80.0, -16.8], [100.0, 0.0]]

tut = turtle.Turtle()
tut.ht()
tut.penup()
tut.sety(-1 * turtle.window_height() / 2 + 20)
text = "You can adjust lines, motion, scale, tessellation size in the code"

#test values
tu = turtle.Turtle()
tu.color("black")
tu.speed(0)
tu.ht()
turtle.tracer(0)

#placeholder used in special effects
deg = 0

create_pattern(tu)
# tut.write(text, align="center", font=("Times New Roman", 15, "italic"))
turtle.update()
while special_effects:
    tu.clear()
    tut.clear()
    sleep(1 / 60)
    create_pattern(tu)
    tut.write(text, align="center", font=("Times New Roman", 15, "italic"))
    turtle.update()
    angle -= .5
    deg = (deg + 1) % 360
    x_offset = scale * cos(2 * radians(deg)) * 1
    y_offset = scale * sin(2 * radians(deg)) * 1
    scale += sin(radians(deg)) * .5 * 0
turtle.done()
