import pygame
import math

def findXCoord(y):
    return width - math.sqrt(radius **2 - ((y-height) ** 2))
def findYCoord(x):
    return height - math.sqrt(radius **2 - ((x-width)**2))

width = 400
height = 400
radius = 400
screen = pygame.display.set_mode((width,height))
white = 255,255,255
blue = 0,0,255
topL = 0,0
bottomR = 400,400
topR = 0,400
bottomL = 400,0
screen.fill(white)
for cord in range(0,400,4):
    pygame.draw.line(screen,blue,(0,cord),(findXCoord(cord),cord))
    pygame.draw.line(screen,blue,(cord,0),(cord,findYCoord(cord)))

pygame.display.flip()
while 1:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
