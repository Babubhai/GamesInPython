import pygame
import random

class obstacles:
    def __init__(self,surface,width,height):
        self.surface = surface
        self.x = [random.randint(0,width-1)  for _ in range(10)]
        self.y = [random.randint(0,height-1) for _ in range(10)]

    def draw(self):
        for i in range(10):
            self.surface.set_at((self.x[i],self.y[i]),(0,255,0))

class food:
    def __init__(self,surface,width,height):
        self.surface = surface
        self.x = [random.randint(0,width-1)  for _ in range(10)]
        self.y = [random.randint(0,height-1) for _ in range(10)]

    def draw(self):
        for i in range(10):
            self.surface.set_at((self.x[i],self.y[i]),(0,0,255))
    

class Worm:
    def __init__(self,surface,x,y,length):
        self.surface = surface
        self.x = x
        self.y = y
        self.length = length
        self.dir_x = 0
        self.dir_y = -1
        self.body= []
        self.obs = []
        self.food = []
        self.last = (0,0)
        self.crashed = False

    def populateFood(self,width,height):
        tx = [random.randint(0,width-1)  for _ in range(50)]
        ty = [random.randint(0,height-1)  for _ in range(50)]
        for i in range(50):
            self.food.append((tx[i],ty[i]))

    def populateObs(self,width,height):
        tx = [random.randint(0,width-1)  for _ in range(50)]
        ty = [random.randint(0,height-1)  for _ in range(50)]
        for i in range(50):
            self.obs.append((tx[i],ty[i]))

    def key_event(self,event):
        if event.key == pygame.K_UP:
            self.length+=10
            self.dir_x = 0
            self.dir_y = -1
        elif event.key == pygame.K_DOWN:
            self.length+=10
            self.dir_x = 0
            self.dir_y = 1
        elif event.key == pygame.K_RIGHT:
            self.length+=10
            self.dir_x = 1
            self.dir_y = 0
        elif event.key == pygame.K_LEFT:
            self.length+=10
            self.dir_x = -1
            self.dir_y = 0
        
    def move(self):
        self.x += self.dir_x
        self.y += self.dir_y
        # one way of checking whether pixel is set on given position or not
        # but not efficient
        if (self.x,self.y) in self.food:
            print "food found"
        elif (self.x,self.y) in self.body:
            self.crashed = True
        elif (self.x,self.y) in self.obs:
            self.crashed = True
        """r,b,g,a = self.surface.get_at((self.x,self.y))
        if (r,g,b) == (0,0,255):
            print "food found"
        elif (r,g,b) == (0,255,0):
            self.crashed = True"""
        
        self.body.insert(0,(self.x,self.y))

        if len(self.body) >= self.length:
            self.last = self.body.pop()
        else:
            self.last = self.body[-1]

    def drawObs(self):
        for x,y in self.food:
            self.surface.set_at((x,y),(0,0,255))
        for x,y in self.obs:
            self.surface.set_at((x,y),(0,255,0))

    def draw(self):
        self.surface.set_at((self.x,self.y),(255,255,255))
        self.surface.set_at(self.last,(0,0,0))
        """for x,y in self.body:
            self.surface.set_at((x,y),(255,255,255))
        for x,y in self.food:
            self.surface.set_at((x,y),(0,0,255))
        for x,y in self.obs:
            self.surface.set_at((x,y),(0,255,0))"""

width = 640
height = 400

screen = pygame.display.set_mode((width,height))
screen.fill((0,0,0))
pygame.display.flip()
clock = pygame.time.Clock()
running = True

w = Worm(screen,width/2,height/2,50)
w.populateObs(width,height)
w.populateFood(width,height)
w.drawObs()
pygame.display.flip()

while running:
    w.draw()
    w.move()

    if w.crashed or w.x <= 0 or w.x >= width-1 or w.y <- 0 or w.y >= height-1:
        print "Crashed"
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            w.key_event(event)
    pygame.display.flip()
    clock.tick(40)
            
