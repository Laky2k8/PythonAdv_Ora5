import random
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((700, 700))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (200,200,200)
DARK_GRAY = (50,50,50)

running = 1

row = 17
column = 17
matrix1 = []

def createMatrix():
    global matrix1
    matrix1 = [[0 for x in range(row)] for y in range(column)]

    for i in range(row):
        for j in range(column):
            matrix1[i][j] = random.randint(0, 1)



createMatrix()

while running:
  for event in pygame.event.get():
    if event.type == QUIT:
      running = 0

  screen.fill(DARK_GRAY)



  blockSize = 40  # Set the size of the grid block
  for x in range(len(matrix1)):
      for y in range(len(matrix1[0])):
          rect = pygame.Rect(x * 40, y * 40, blockSize, blockSize)
          if matrix1[y][x] == 1:
              pygame.draw.rect(screen, DARK_GRAY, rect, 0)
          else:
              pygame.draw.rect(screen, LIGHT_GRAY, rect, 0)


  pygame.display.flip()

pygame.quit()



