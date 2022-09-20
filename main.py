from re import T
import pygame
import random
import math

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
mines = []
gameRunning = True

class Grid:
    # Grid Class contains info for individual points on grid
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.clickCheck = False
        self.mine = False
        self.flag = False
        # number of surrounding mines
        self.adjacentMines = 0
        self.rect = pygame.Rect(self.xPos * imgSize, self.yPos * imgSize, imgSize, imgSize)
    
    def displayGrid(self):
        if self.mine == False and self.flag == True and gameRunning == False:
            screen.blit(mineFalse, self.rect)
        else:
            if self.clickCheck == True:
                if self.mine == True and self.flag == False:
                    screen.blit(mineClicked, self.rect)
                else:
                    if self.adjacentMines == 0:
                        screen.blit(empty, self.rect)            
                    elif self.adjacentMines == 1:
                        screen.blit(grid1, self.rect)
                    elif self.adjacentMines == 2:
                        screen.blit(grid2, self.rect)
                    elif self.adjacentMines == 3:
                        screen.blit(grid3, self.rect)
                    elif self.adjacentMines == 4:
                        screen.blit(grid4, self.rect)
                    elif self.adjacentMines == 5:
                        screen.blit(grid5, self.rect)
                    elif self.adjacentMines == 6:
                        screen.blit(grid6, self.rect)
                    elif self.adjacentMines == 7:
                        screen.blit(grid7, self.rect)
                    elif self.adjacentMines == 8:
                        screen.blit(grid8, self.rect)
            else:
                if self.flag == True:
                    screen.blit(flag, self.rect)
                elif self.mine == True and gameRunning == False:
                    screen.blit(mine,self.rect)
                else:
                    screen.blit(grid0, self.rect)
    

    def getAdjacentMines(self):
        if self.mine == False:
            for x in range(self.xPos-1, self.xPos+2):
                if x >= 0 and x < horGrid:
                    for y in range(self.yPos-1, self.yPos+2):
                        if y >= 0 and y < verGrid:
                            if grid[x][y].mine == True:
                                self.adjacentMines += 1


    def emptyClick(self):
        if self.adjacentMines == 0:
            self.clickCheck = True
            for x in range(self.xPos-1, self.xPos+2):
                if x >= 0 and x < horGrid:
                    for y in range(self.yPos-1, self.yPos+2):
                        if y >= 0 and y < verGrid:
                            if grid[x][y].adjacentMines == 0:
                                grid[x][y].clickCheck = True


def createGrid():

    # Initializing mines
    for i in range(0, numMines):
        dupeCheck = True
        x = random.randint(0, horGrid-1)
        y = random.randint(0, verGrid-1)

        # Checking for duplicate grid positions
        while dupeCheck:
            if (x, y) in mines:
                x = random.randint(0, horGrid-1)
                y = random.randint(0, verGrid-1)
            else:
                dupeCheck = False

        mines.append((x, y))

    # Initializing grid
    for x in range(0, horGrid):
        line = []
        for y in range(0, verGrid):
            line.append(Grid(x, y))
            if (x, y) in mines:
                line[y].mine = True

        grid.append(line)


def main():
    
    # Creating grid and setting up mines values
    createGrid()
    for i in grid:
        for j in i:
            j.getAdjacentMines()

    while gameRunning:
        clock.tick(60)

        # Displaying Grid
        for i in grid:
            for j in i:
                j.displayGrid()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            # Handling Player Inputs
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = math.floor(event.pos[0]/32)
                y = math.floor(event.pos[1]/32)

                # Left Click
                if event.button == 1:
                    if grid[x][y].flag == False:
                        grid[x][y].clickCheck = True
                        grid[x][y].emptyClick()

                # Right Click
                if event.button == 3:
                    if grid[x][y].clickCheck == False and grid[x][y].flag == False:
                        grid[x][y].flag = True
                    elif grid[x][y].flag == True:
                        grid[x][y].flag = False
        
        clock.tick(60)



main()