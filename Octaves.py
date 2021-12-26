"""
Sep 22, 2021
Title: Octaves
@author: Bekah Smith

Description: A stylized piano is generated, depicting 4 octaves of notes as 4 concentric circles.
Notes are chosen at random and shaded in with a colors, creating one chord on each octave.

"""

import turtle
import random, time

# =================== DEFINE CLASSES =========================

class Start():
    def __init__(self):
    # Creating a panel to draw on
        self.panel = turtle.Screen()
        self.panel.setup(width=700, height=700)
        self.panel.bgcolor("white")
        turtle.colormode(255)
        turtle.tracer(0) # turn off turtles' animation 
        
        Web(self.panel)

class Web(turtle.Turtle):
    def __init__(self, panel):  
        super().__init__(visible=False)
        self.panel = panel
        self.up()
        self.width(3)
        self.pencolor("black")
        self.length = 17
        self.angle = 360/7 # Changed from original pentagon design to heptagon
        self.forward(43) # move out of the center to prepare for drawing webs
        self.left(140)
        
        self.draw_all()
        
    def draw_all(self):
        # Web design borrowed from Jack Seliskar https://drive.google.com/drive/u/1/folders/1TOcGo8msaZ1wEbiz75ABsVrHypVciL5w
        for polyside in range(5): # repeats 3 times
            self.down()
            self.draw_polygon(self.length) # each iteration of the for loop, the defined shape will be drawn
            self.length = self.length + 6 # changes the value of length each iteration
            self.left(6)
            self.up()
            self.forward(6) # wiggles webber to a slightly new location and heading
            self.right(90)
            self.forward(6)
            self.left(90)
            
        Piano(self.panel)
        
    def draw_polygon(self, length): # defines the shape which will be repeated
        for polygon in range(7): # repeats for range 0-6
            self.down()
            self.forward(self.length)
            self.left(self.angle)
            self.up()
        # End borrowed code - thank you, Jack!

class Piano(turtle.Turtle):
    def __init__(self, panel): 
        super().__init__(visible=False)
        self.panel = panel
        self.up()
        self.width(6)
        self.pencolor("black")
        
        self.circles()
        
    def circles(self):
        self.ir = 50 # inner radius, static
        self.r = 50 # first circle radius
        self.rMod = 50 # added to size of circle's radius each iteration
        
        for i in range(5): # take circler outside of the middle, then draw 5 circles to represent pianos
            self.forward(self.ir)
            self.left(90)
            self.down()
            self.circle(self.r)
            self.right(90)
            self.up()
            self.r += self.rMod # adds the value of rMod to r each time so the rings will grow

        self.up()
        
        self.lines()

    def lines(self):
        self.keyWidth = 360/12 # width dividing 12 equal-length black and white keys
        self.keyPositions = [] # create a list to store all the key start positions
        self.headings = [] # create a list to store all of turtle's headings at these positions
        
        for i in range(12): # repeats 12 lines to draw 12 lines dividing keys
            self.up()
            self.goto(0,0)
            self.right(self.keyWidth)
            self.forward(self.ir) # start drawing lines at first ring
            self.down()
            self.keyPositions.append(self.pos()) # appends the current position of liner to the list of starting key positions
            self.headings.append(self.heading()) # appends the current heading of liner to the list of turtle headings that correspond to each key position
            self.forward(200)
            
        self.up()
        
        Flats(self.panel, self.keyPositions, self.headings, self.rMod, self.keyWidth)

class Flats(turtle.Turtle):
    def __init__(self, panel, keys, heads, mod, width): 
        super().__init__(visible=False)
        self.keyPositions = keys
        self.headings = heads
        self.rMod = mod
        self.keyWidth = width
        self.panel = panel
        self.up()
        self.width(6)
        self.pencolor("black")
        
        self.flat_define()
        
    def flat_define(self):
        # list designate the start locations of the black keys
        self.flats = [self.keyPositions[0], self.keyPositions[2], self.keyPositions[5], self.keyPositions[7], self.keyPositions[9]]
        # list shows the corresponding headings for the turtle drawing each set of black keys
        self.flatHeads = [self.headings[0], self.headings[2], self.headings[5], self.headings[7], self.headings[9]]
        
        for i in range(5): # loop will run 5 times, to use each variable in the above lists in turn
            self.fillcolor("black")
            self.goto(self.flats[i])
            self.setheading(self.flatHeads[i])
            self.down()
            
            self.draw_flats() # draws the black keys on the keyboard
            
        Chords(self.panel, self.keyPositions, self.headings, self.rMod, self.keyWidth)
        
    def draw_flats(self): # define the shape of 4 black keys filled in together
        self.down()
        self.begin_fill()
        self.forward(200)
        self.left(90)
        self.circle(self.rMod * 5, self.keyWidth) #draws the curve of the key 
        self.left(90)
        self.forward(200)
        self.right(90)
        self.circle(self.rMod, -self.keyWidth) # moves filler backwards so that curve is parallel to first
        self.end_fill()
        self.up()

class Chords(turtle.Turtle):
    def __init__(self, panel, keys, heads, mod, width): 
        super().__init__(visible=False)
        self.keyPositions = keys
        self.headings = heads
        self.rMod = mod
        self.keyWidth = width
        self.panel = panel
        self.up()
        self.width(6)
        self.pencolor("black")
        self.colors = [(255,109,0), (255,121,0), (255,133,0), (255, 145, 0), (255,158,0), (36,0,70), (60,9,108), (90, 24, 154), (123, 44, 191), (157,78,221)]
        
        self.notes()
        
    def keyfill(self, row): # defines the shape of individual keys to be filled in, with variable widths for different rows
        self.row = row
        self.down()
        self.begin_fill()
        self.forward(self.rMod)
        self.left(90)
        self.circle(self.rMod * (self.row+1), self.keyWidth) # uses current row to modify size of key fill
        self.left(90)
        self.forward(self.rMod)
        self.right(90)
        self.circle(self.rMod * self.row, -self.keyWidth)
        self.end_fill()
        self.up()
    
    # filling in random keys with random colors on the first row
    def notes(self):
        for row in range(1,5): # this loop asks filler to go through each of the 4 rows (octave)
            for notes in range(1,5): # this loop asks filler to go through 4 notes for each row
                self.fillcolor(random.choice(self.colors)) # choose a random color
                y = random.randint(0,11) # choose a random integer for the index in next two lines
                self.goto(self.keyPositions[y])
                self.setheading(self.headings[y])
                self.forward(self.rMod * (row-1))
                self.keyfill(row) # fills in the key with a random color
                time.sleep(.3) #creates an animation of the keys being filled in.
                self.panel.update()
            
        self.up()
        
# =================== RUN THE PROGRAM =========================

if __name__=='__main__':
    Start()
    turtle.mainloop()
