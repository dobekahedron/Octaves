"""
Sep 22, 2021
PC04 Generative Art
@author: Bekah Smith

Description: A stylized piano is generated, depicting 4 octaves of notes in 4 circles.
Notes are chosen at random and shaded in with a colors, creating one chord on each octave.
Goal to invoke feelings of structure and randomness together.

"""

import turtle
import math, random, time #time is NEW!!!

turtle.colormode(255)
turtle.tracer(0) # turn off turtles' animation 

# Creating a panel for 4 turtles to draw on
panel = turtle.Screen()
w = 700 # width of panel
h = 700 # height of panel

panel.bgcolor("white")

turtle.hideturtle()
webber = turtle.Turtle()
circler = turtle.Turtle()
liner = turtle.Turtle()
filler = turtle.Turtle()

colors = [(255,109,0), (255,121,0), (255,133,0), (255, 145, 0), (255,158,0), (36,0,70), (60,9,108), (90, 24, 154), (123, 44, 191), (157,78,221)]

# get turtles ready with color, thickness, etc

circler.hideturtle()
circler.up()
circler.width(6)
circler.pencolor("black")

liner.hideturtle()
liner.up()
liner.width(6)
liner.pencolor("black")

filler.hideturtle()
filler.up()
filler.width(6)
filler.pencolor("black")
filler.fillcolor("black")

webber.hideturtle()
webber.up()
webber.width(3)
webber.pencolor("black")
webber.forward(43) # move out of the center to prepare for drawing webs
webber.down()

# Web design borrowed from Jack Seliskar Pseudocode https://drive.google.com/drive/u/1/folders/1TOcGo8msaZ1wEbiz75ABsVrHypVciL5w

length = 17
angle = 360/7 # Changed from original pentagon design to heptagon
webber.left(140)

def draw_polygon(length): # defines the shape which will be repeated
    for polygon in range(7): # repeats for range 0-6
        webber.down()
        webber.forward(length)
        webber.left(angle)
        webber.up()
        
for polyside in range(5): # repeats 3 times
    turtle.down()
    draw_polygon(length) # each iteration of the for loop, the defined shape will be drawn
    length = length + 6 # changes the value of length each iteration
    webber.left(6)
    webber.up()
    webber.forward(6) # wiggles webber to a slightly new location and heading
    webber.right(90)
    webber.forward(6)
    webber.left(90)
    
# End borrowed pseudocode - thank you, Jack!

ir = 50 # inner radius, static
r = 50 # first circle radius
rMod = 50 # added to size of circle's radius each iteration

for it1 in range(5): # take circler outside of the middle, then draw 5 circles to represent pianos
    circler.forward(ir)
    circler.left(90)
    circler.down()
    circler.circle(r)
    circler.right(90)
    circler.up()
    r += rMod # adds the value of rMod to r each time so the rings will grow

circler.up()

keyWidth = 360/12 # width dividing 12 equal-length black and white keys
keyPositions = [] # create a list to store all the key start positions
headings = [] # create a list to store all of turtle's headings at these positions

for it2 in range(12): # repeats 12 lines to draw 12 lines dividing keys
    liner.up()
    liner.goto(0,0)
    liner.right(keyWidth)
    liner.forward(ir) # start drawing lines at first ring
    liner.down()
    keyPositions.append(liner.pos()) # appends the current position of liner to the list of starting key positions
    headings.append(liner.heading()) # appends the current heading of liner to the list of turtle headings that correspond to each key position
    liner.forward(200)
    
liner.up()

def draw_flats(): # define the shape of 4 black keys filled in together
    filler.down()
    filler.begin_fill()
    filler.forward(200)
    filler.left(90)
    filler.circle(rMod * 5,keyWidth) #draws the curve of the key 
    filler.left(90)
    filler.forward(200)
    filler.right(90)
    filler.circle(rMod,-keyWidth) # moves filler backwards so that curve is parallel to first
    filler.end_fill()
    filler.up()

# list designate the start locations of the black keys
flats = [keyPositions[0], keyPositions[2], keyPositions[5],keyPositions[7],keyPositions[9]]
# list shows the corresponding headings for the turtle drawing each set of black keys
flatHeads = [headings[0], headings[2], headings[5], headings[7], headings[9]]

for i in range(5): # loop will run 5 times, to use each variable in the above lists in turn
    filler.fillcolor("black")
    filler.goto(flats[i])
    filler.setheading(flatHeads[i])
    filler.down()
    draw_flats() # draws the black keys on the keyboard
    filler.up()

def keyfill(row): # defines the shape of individual keys to be filled in, with variable widths for different rows
    filler.down()
    filler.begin_fill()
    filler.forward(rMod)
    filler.left(90)
    filler.circle(rMod * (row+1),keyWidth) # uses current row to modify size of key fill
    filler.left(90)
    filler.forward(rMod)
    filler.right(90)
    filler.circle(rMod * row,-keyWidth)
    filler.end_fill()
    filler.up()

# filling in random keys with random colors on the first row

for row in range(1,5): # this loop asks filler to go through each of the 4 rows (octave)
    for notes in range(1,5): # this loop asks filler to go through 4 notes for each row
        filler.fillcolor(random.choice(colors)) # choose a random color
        y = random.randint(0,11) # choose a random integer for the index in next two lines
        filler.goto(keyPositions[y])
        filler.setheading(headings[y])
        filler.forward(rMod * (row-1))
        keyfill(row) # fills in the key with a random color
        time.sleep(.3) # NEW !!!!
        panel.update() # turned off animation NEW !!!
    
filler.up()
#panel.update() # turned off animation 
# =================== CLEAN UP =========================
turtle.done()

'''
I showed the output of this code to a couple of people to get advice on the artwork.
First piece of advice, from Sergio, was to add music to correspond with the notes.
Otherwise he seemed very complimentary about how it looked.
I asked a friend of mine to give critical feedback, but this time did not provide any context about what the art represented.
My friend can code a little bit. He thought it was cool, that it could use more black because it breaks up the bulls-eye shape.
He also suggested that the circle shape is cool, but it might look better if it was broken up a bit.
I think it is very uniform and too clean, so I appreciated his critique on ways to enhance the artwork.
I think it would be fun to try to take his feedback by stamping the keys, with slightly random tilts,
it could be lots more interesting if all the keys are askew.

'''