# from turtle import window_width


alien = Actor('alien')
# alien.pos = 120, 56
alien.topright = 0, 75


WIDTH = alien.width + 300
HEIGHT = alien.height + 150

def draw():
    screen.clear()
    alien.draw()

def update():
    alien.left += 5
    # alien.right += 5
    if alien.right > WIDTH:
       alien.right = 0
    

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        print("Eek!")
    else:
        print("You missed me!")