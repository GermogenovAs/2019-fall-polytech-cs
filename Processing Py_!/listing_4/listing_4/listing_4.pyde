windowWidth = int(500)
windowHeight = int(500)
ellipseSize = int(100)

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
