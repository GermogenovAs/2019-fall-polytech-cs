def setup():
    size(500, 500)
    smooth()
    background(255)
    noStroke()
    noLoop()
    
    
def draw():
    for i in range(10):
        for k in range(5):
            fill(i*20)
            rect(i*40+50,50+(k)*80,35,35)
            fill(220-i*20)
            rect(i*40+50,90+(k)*80,35,35)
