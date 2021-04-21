import pygame

pygame.init()

def doesEventTypeEqualQuit(eventType):
    return eventType == pygame.QUIT

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Worm")
icon = pygame.image.load('worm.png')
pygame.display.set_icon(icon)

playerImage = pygame.image.load('candy-worm.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

def player(x, y):
    screen.blit(playerImage, (x, y))

running = True
while running:
    for event in pygame.event.get():
        if doesEventTypeEqualQuit(event.type):
                running = False
    screen.fill((150,255, 65))
    player(playerX, playerY)
    pygame.display.update()
