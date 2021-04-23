import pygame

pygame.init()

def isEventTypeRight(key):
    return key == pygame.K_RIGHT

def isEventTypeLeft(key):
    return key == pygame.K_LEFT

def isEventTypeUp(key):
    return key == pygame.K_UP

def isEventTypeDown(key):
    return key == pygame.K_DOWN

def doesEventTypeEqualQuit(eventType):
    return eventType == pygame.QUIT


def doesEventTypeEqualKeyUp(event):
    global playerX_change
    global playerY_change
    if event.type == pygame.KEYUP:
        print("A key was released")
        wasXReleased = isEventTypeLeft(event.key) or isEventTypeRight(event.key)
        if wasXReleased:
            playerX_change = 0
        wasYReleased = isEventTypeDown(event.key) or isEventTypeUp(event.key)
        if wasXReleased:
            playerY_change = 0

def doesEventTypeEqualKeyDown(event):
    global playerX_change
    global playerY_change
    if event.type == pygame.KEYDOWN:
        if isEventTypeLeft(event.key):
            playerX_change = -0.1
        elif isEventTypeRight(event.key):
            playerX_change = 0.1
        elif isEventTypeDown(event.key):
            playerY_change = -0.1
        elif isEventTypeUp(event.key):
            playerY_change = 0.1
        return True

X_AXIS = 800
Y_AXIS = 600
screen = pygame.display.set_mode((X_AXIS, Y_AXIS))

pygame.display.set_caption("Worm")
icon = pygame.image.load('worm.png')
pygame.display.set_icon(icon)

playerImage = pygame.image.load('candy-worm.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0
ICON_SIZE = 64
MAX_X_AXIS = X_AXIS - ICON_SIZE

def player(x, y):
    screen.blit(playerImage, (x, y))

running = True
while running:

    screen.fill((150,255, 65))

    for event in pygame.event.get():
        if doesEventTypeEqualQuit(event.type):
            running = False
        elif doesEventTypeEqualKeyDown(event):
            print("A key was pressed!")
        elif doesEventTypeEqualKeyUp(event):
            print("Left or Right key was released")
        
    
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= MAX_X_AXIS:
        playerX = MAX_X_AXIS
    player(playerX, playerY)
    pygame.display.update()
