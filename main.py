import pygame

pygame.init()
screen = pygame.display.set_mode((400, 800))
pygame.display.set_caption("Mineswapper :D")
clock = pygame.time.Clock()
    
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             exit()
    
    pygame.display.update()
    clock.tick(60)
