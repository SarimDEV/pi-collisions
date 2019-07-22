import pygame
pygame.init()

clock = pygame.time.Clock()

winWidth = 500
winHeight = 500
timeSteps = 20

win = pygame.display.set_mode((winWidth, winHeight))
font = pygame.font.SysFont(None, 25)
pygame.display.set_caption("Calcuating Pi")

count = 0

class box(object):
    def __init__(self, x, w, h, m, v):
        self.w = w
        self.h = h
        self.x = x
        self.y = winHeight-self.h
        self.m = m
        self.v = v
        
    def draw(self, win):
        self.x += self.v
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.w, self.w))

def collision(box0, box1):
    if(box0.x + box0.w <= box1.x or box0.x >= box1.x + box1.w):
        pass
    else:
        v1 = box0.v
        v2 = box1.v
        m1 = box0.m
        m2 = box1.m

        v1_final = (((m1-m2)/(m1+m2))*v1) + (((2*m2)/(m1+m2))*v2)
        v2_final = (((m2-m1)/(m1+m2))*v2) + (((2*m1)/(m1+m2))*v1)
            
        box0.v = v1_final
        box1.v = v2_final
        incrementCounter()

def wallCollision(box):
    if(box.x <= 0):
        box.v *= -1
        incrementCounter()

def incrementCounter():
    global count
    count += 1

def counterDisplay(count):
    text = font.render("# Collisions: " + str(count), True, (255,255,255))
    win.blit(text, [winWidth-200, 100])
        

box0 = box(winWidth-100, 100, 100, 100, -2/timeSteps)
box1 = box(winWidth-300, 50, 50, 1, 0)


run = True
while run:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for x in range(timeSteps):
        win.fill(0)
        
        box0.draw(win)
        box1.draw(win)

        collision(box0, box1)
        wallCollision(box1)

        counterDisplay(count)


        pygame.display.update()

pygame.quit()
