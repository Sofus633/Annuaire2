from ball import Ball
import pygame
from settings import screen
from texte import Texte
from settings import backgroundcolor



def display_things(things):
    for thing in things:
        if type(thing) == Ball:
            #affichage ligne entre balles
            for ball in things:
                if type(thing) == Ball and ball.nom == None:
                    #distance manhatan
                    if (abs(ball.position[0] - thing.position[0]) + abs(ball.position[1] - thing.position[1])) < 100:
                        pygame.draw.line(screen, ball.color, (ball.position[0], ball.position[1]), (thing.position[0], thing.position[1]), 1)
            
            #draw ball         
            pygame.draw.circle(screen, thing.color, (thing.position[0], thing.position[1]), thing.radius)
            
            #TEMP drawn name / number
            if thing.display:
                screen.blit(thing.font.render(str(f"{thing.nom}\n{thing.num}"), False, (255, 255, 255)), (thing.position[0], thing.position[1]))

            #for testing : draw expected destination of a ball 
            if thing.destination != None:
                #pygame.draw.circle(screen, (0, 255, 0), (thing.destination[0], thing.destination[1]), 10)
                pass
            
        #draw text (mainly for animations)
        if type(thing) == Texte:
            screen.blit(thing.textvis, (thing.position[0], thing.position[1]))
            
    pygame.display.flip()
    screen.fill(backgroundcolor)
    
def put(tab, toadd, index):
    for obj in toadd:
        tab.insert(index if not index else -1, obj)
    
    