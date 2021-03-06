import pygame
from pygame.locals import *
from Button import Button

def itemDrawButtons(data, pos):
    for button in data.buttons:
        button.draw(pos, data.screen)

def itemProcessClick(data, pos):
    for button in data.buttons:
        msg = button.check(pos)
        if msg != None:
            if msg == "Back":
                data.mode = "battleMode"
            elif msg == "Quit":
                pygame.quit()
                return False
            else:
                data.mode = "battleMode"
    return True

def itemModeButtons(data):
    buttonW = 200
    buttonH = 50
    data.buttons = {
                    Button("Item1", data.windowSize[0]//10 - buttonW//2,
                           data.windowSize[1]//10 - buttonH//2,
                           buttonW, buttonH, (0, 0, 255), (255, 0, 255)),
                    Button("Item2", data.windowSize[0]//10 - buttonW//2,
                           data.windowSize[1]//10 + buttonH//2,
                           buttonW, buttonH, (0, 0, 255), (255, 0, 255)),
                    Button("Back", data.windowSize[0]//10 - buttonW//2,
                           data.windowSize[1]//10 + 3*buttonH//2,
                           buttonW, buttonH, (0, 0, 255), (255, 0, 255)),
                    Button("Quit", data.windowSize[0]//10 - buttonW//2,
                           data.windowSize[1]//10 + 5*buttonH//2,
                           buttonW, buttonH, (0, 0, 255), (255, 0, 255))
                    }

def itemModeEvents(data):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            return False
        elif event.type == KEYDOWN:
            pass            
        elif event.type == MOUSEBUTTONDOWN:
            # make some kind of move?
            pass
    return True
