import pygame
from objects.rect import Rect
pygame.font.init()

# GENERAL VARIABLES
gameW, gameH = 900, 600
playerW, playerH = 60, 120
gridLength = 5

# COLORS
black = (0,0,0)
grey = (128,128,128)
miniGrey = (178, 178, 178)
yellow = (255,255,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
lightPurple = (86, 95, 120)

# FONTS
muli = {
    "15": pygame.font.Font("fonts/muli.ttf",15),
    "20": pygame.font.Font("fonts/muli.ttf",20),
    "30": pygame.font.Font("fonts/muli.ttf",30),
    "70": pygame.font.Font("fonts/muli.ttf",70)
}

# WASD
W, A, S, D = 0, 1, 2, 3

# STATES
AUTHORS = 0
START = 1
GAME = 2
PAUSE = 3
GAMEOVER = 4

# PAUSELOCK STATES
pauseNone = 0
pauseEnter = 1
pauseExit = 2

# DOOR
doorSlim, doorWide = 100, 150
LRDoor = (gameH - doorWide) / 2
TBDoor = (gameW - doorWide) / 2

# CLEAR ZONES
clearZones = {
    "w": Rect(gameW/2 - doorWide/2 + 50,10,doorWide - 100,5,grey),
    "a": Rect(110,gameH/2 - doorWide/2 + 50,5,doorWide - 100,grey),
    "s": Rect(gameW/2 - doorWide/2 + 50,485,doorWide - 100,5,grey),
    "d": Rect(785,gameH/2 - doorWide/2 + 50,5,doorWide - 100,grey)
}

# ENEMY DATA   HP,FIRE RATE IN TICKS (1/60),DMG
enemyData = {
    "apple": [60,60,3,40,1],
    "cherry": [60,60,1,20,1],
    "banana": [60,60,5,60,1],
    "peep": [120,120,15,60,2],
    "bunny": [60,60,1,60,1]
}

# ITEM DESCRIPTIONS
itemDescriptions = [
    None,
    None,
    None,
    "Faster fire",
    "Speed boost",
    None,
    None,
    "Full HP + 1",
    "Attack boost",
    None
]
