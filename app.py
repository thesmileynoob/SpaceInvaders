"""
The main game loop
"""
import time, sys, pygame

pygame.init()

size = width, height = 650,700

screen = pygame.display.set_mode(size)

while True:
    screen.fill((100,0,0))
    pygame.display.flip()    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    time.sleep(0.1)
    screen.fill((0,0,100))        
    pygame.display.flip()
    time.sleep(0.1)
    
