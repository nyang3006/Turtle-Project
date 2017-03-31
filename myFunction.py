def tear(t):
    for times in range(10):
        t.circle(times * 2)
        t.left(10)
        t.forward(10)
        
def L(t,distance,angle):
    t.forward(distance)
    t.left(angle)
    t.forward(distance)
    
#Creates any shape
def polygon(t, sides, distance):
    angle = 360 / sides
    #t.begin_fill()
    for times in range(sides):
        t.forward(distance)
        t.left(angle)
    #t.end_fill()

#Creates a triangle inside of a square
def cool(t,distance):
    t.color("teal")
    polygon(t,4,distance)
    t.color("lightblue")
    polygon(t,3,distance)
#Creates 4 "cool" shapes
def coolSquared(t,distance):
    for times in range(4):
         cool(t,distance)
         t.right(90)

def jump(t,x,y):
    t.pu()
    t.goto(x,y)
    t.pd()

#Creates a dumbell
def dumbell(t, size):
    t.width(10)
    t.begin_fill()
    t.circle(size/2)
    t.forward(size*2)
    t.right(180)
    t.circle(size/2)
    t.end_fill()
#Creates a spiral made up of stars
def starspiral(t):
 for times in range(255):
        c=(times,times,255-times)
        t.color(c)
        t.width(3)
        polygon(t,1,25)
        t.left(145)
        t.forward(255-times)
        print(c)
#Creates a spiral made up of squares
def squarespiral(t):
    for times in range(256):
        c=(times,255-times,0)
        t.color(c)
        print(c)
        polygon(t,4,50)
        t.left(50)
        t.forward(times)
