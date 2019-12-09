stepX = 0
stepY = 0

def setup():
    size(500, 500)
    background(0)
    
    
def draw():
    colorMode(HSB, width, height, 100)
    
    global stepX
    global stepY
    
    stepX = mouseX+2
    stepY = mouseY+2
    for gridY in range(0, height, stepY):
        for gridX in range(0, width, stepX):
            stroke(gridX, height-gridY, 100)
            strokeWeight(stepX)
            line(gridX, gridY, stepX+gridX, stepY+gridY)
