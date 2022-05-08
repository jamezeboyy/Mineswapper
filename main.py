import pygame
import random

# Window size setup (will be changed later to easily change difficulty in game)
imgSize = 32
verGrid = 10
horGrid = 10
numMines = 9
WHITE = (200, 200, 200)
HEIGHT = verGrid*imgSize
WIDTH = horGrid*imgSize

# Initial Setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mineswapper :D")
clock = pygame.time.Clock()

#Setting up assets
empty = pygame.image.load("Assets/empty.png")
flag = pygame.image.load("Assets/flag.png")
grid0 = pygame.image.load("Assets/Grid.png")
grid1 = pygame.image.load("Assets/grid1.png")
grid2 = pygame.image.load("Assets/grid2.png")
grid3 = pygame.image.load("Assets/grid3.png")
grid4 = pygame.image.load("Assets/grid4.png")
grid5 = pygame.image.load("Assets/grid5.png")
grid6 = pygame.image.load("Assets/grid6.png")
grid7 = pygame.image.load("Assets/grid7.png")
grid8 = pygame.image.load("Assets/grid8.png")
mine = pygame.image.load("Assets/mine.png")
mineClicked = pygame.image.load("Assets/mineClicked.png")
mineFalse = pygame.image.load("Assets/mineFalse.png")


# Global variable
grid = []


class Grid:
    # Grid Class contains info for individual points on grid
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.clicked = False
        self.mine = False
        self.flag = False
        # number of surrounding mines
        self.value = 0
        self.rect = pygame.Rect(self.xPos * imgSize, self.yPos * imgSize, imgSize, imgSize)
    
    def drawGrid(self):
        screen.blit(grid0, self.rect)


# Global variable
grid = []
mines = []

def createGrid():
    for x in range(0, horGrid):
        line = []
        for y in range(0, verGrid):
            line.append(Grid(x, y))
        grid.append(line)

def main():
    createGrid()

    while True:
        clock.tick(60)

        # Displaying Grid
        for i in grid:
            for j in i:
                j.drawGrid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        pygame.display.update()
        clock.tick(60)



main()