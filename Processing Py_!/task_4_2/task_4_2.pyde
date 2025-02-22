def setup():
    size(600, 600)
    noLoop()
    
    
def draw():
    
    background(100)
    smooth()
    strokeWeight(50)
    stroke(200)
    
    translate(width/2, height/2 - 100)
    line(-100, 0, 100, 0)
    
    translate(0, 100)
    scale(1.5, 1.5)
    line(-100, 0, 100, 0)
    
    scale(0.7, 0.7)
    translate(0, -200)
    scale(1.5, 1.5)
    line(-100, 0, 100, 0)
