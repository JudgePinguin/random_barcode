import random

BLACK   = color(0)
GRAY_50 = color(127)
WHITE   = color(255)

barcode_Colors = [BLACK,GRAY_50,WITE]



def setup():
    size(1280,720)
    background()
    
def draw():
    x = random.randint(0,width)
    w = random.randint(1,50)
    c = random.choice([BLACK, WHITE)
    
    
    fill(c)
    noStroke()
    rect(x, 0, w, height)
    
