def setup():
    size(500, 500)
    smooth()
    noLoop()
    noStroke()
    ellipseMode(CENTER)
    
    
def draw():
    background(255)
    border = float(50)             #50
    nw = float(width - 2*border)   #400
    nh = float(height - 2*border)  #400
    number = 5
    nWstep = nw/number #80
    nHstep = nh/number #80
    for i in range(number):
        for j in range(number):
            x = border + j*nWstep+nWstep/2
            y = border + i* nHstep+nHstep/2
            size = float(5 + (j+i)*10)
            mColor = float(size*1.5)
            fill(20, 50, mColor)
            ellipse(525-x, 525-y, size, size)
            fill(250)
            ellipse(525-x,525-y,3,3)
            
