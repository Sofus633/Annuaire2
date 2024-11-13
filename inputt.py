import pygame

def inputt(expected, events):
    tab = []
    for event in events:
            if event.type == pygame.KEYDOWN and (chr(event.key) in expected or expected == "all"):
                tab.append(chr(event.key))
    return tab

                        