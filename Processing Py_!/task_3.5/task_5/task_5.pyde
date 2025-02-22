windowWidth = int(750)
windowHeight = int(750)
ellipseSize = int(200)

def setup(): 
    size(windowWidth, windowHeight)
    smooth()
    background(255)
    fill(50, 80)
    stroke(100)
    strokeWeight(3)
    noLoop()
    
    
def draw():
    ellipse(windowWidth/2, windowHeight/2 - ellipseSize/2, ellipseSize, ellipseSize)
    ellipse(windowWidth/2 - ellipseSize/2, windowHeight/2, ellipseSize, ellipseSize)
    ellipse(windowWidth/2 + ellipseSize/2, windowHeight/2, ellipseSize, ellipseSize)
    ellipse(windowWidth/2, windowHeight/2 + ellipseSize/2, ellipseSize, ellipseSize)
