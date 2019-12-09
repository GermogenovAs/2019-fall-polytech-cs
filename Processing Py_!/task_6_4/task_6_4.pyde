def setup():
    size(500, 500)
    smooth()
    background(150)
    strokeWeight(1)
    

flug = 1

def draw():
    global flug
    fill(flug, random(0, 30))
    sizeY2 = random(-10, 10)*20
    sizeX2 = random(-10, 10)*20
    ellipse(mouseX, mouseY, sizeX2, sizeY2)

def keyPressed():
    global flug
    
    if(key=='w'):
        flug = 255
        
    if(key=='b'):
        flug = 0
        
    if (key == 'a'):
        saveFrame("myProcessing.pngwwbbbbbbb")
    
