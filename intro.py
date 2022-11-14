#this python file requires pgzero - installation instructions: https://pygame-zero.readthedocs.io/en/latest/installation.html

alien = Actor('alien') #the actor points to the png file in /images/alien.png

alien.topright = 0, 75


WIDTH = alien.width + 300 #sets the window width in relation to the sprite
HEIGHT = alien.height + 150 #sets the window height  in relation to the sprite

def draw():
    screen.clear()
    alien.draw()

def update(): #update every frame
    alien.left += 5 #moves sprint along the screen
    if alien.right > WIDTH: #checks to see when sprite reaches end of window
       alien.right = 0
    

def on_mouse_down(pos):  #this function is checking to see when the mouse cursor position matches the sprite position to simulate an impact
    if alien.collidepoint(pos): 
        alien.image = 'alien_hurt'
        print("Eek!")
    else:
        print("You missed me!")
