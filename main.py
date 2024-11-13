import pygame
from inputt import inputt
from displays import display_things, put
from settings import clock
from ball import createballcircle, update_ball

todisplay = []
balls = []



def mainloop():
    running = True
    while running:
        accueille()
        break
        #annuaire()
        
        
def accueille():
    running = True
    todisplay = []
    balls = createballcircle((500, 500))
    animations = []
    put(todisplay, balls, 0)

    while running:
        event = pygame.event.get()
        if "e" in inputt("e", event):
            running = False
        
        
        display_things(todisplay)
        update_ball(balls)
        clock.tick(60)  

mainloop()