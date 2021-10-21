import random
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Python Advanced 5.: Game Thing ")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (200,200,200)
DARK_GRAY = (50,50,50)

running = 1

plr = pygame.sprite
plr.image = pygame.image.load('player.png')
plrX = 0
plrY = 0

keys = [0,0,0,0]

row = 17
column = 17
matrix1 = []

def createMatrix():
    global matrix1
    matrix1 = [[0 for x in range(row)] for y in range(column)]

    for i in range(row):
        for j in range(column):
            matrix1[i][j] = random.randint(0, 1)

    matrix1[0][0] = 0


class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(255,255,255)
        self.image.set_colorkey(255,255,255)

        pygame.draw.rect(self.image,
                         color,
                         pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()



createMatrix()

plr.mask = pygame.mask.from_threshold(plr.image, pygame.Color('yellow'), (1, 1, 1, 255))

while running:
  for event in pygame.event.get():
    if event.type == QUIT:
      running = 0
    elif event.type == KEYDOWN:
        if event.key == K_w or event.key == K_UP:
            keys[0] = 1
        if event.key == K_s or event.key == K_DOWN:
            keys[1] = 1
        if event.key == K_a or event.key == K_LEFT:
            keys[2] = 1
        if event.key == K_d or event.key == K_RIGHT:
            keys[3] = 1
        print(keys)

    elif event.type == KEYUP:
        if event.key == K_w or event.key == K_UP:
            keys[0] = 0
        if event.key == K_s or event.key == K_DOWN:
            keys[1] = 0
        if event.key == K_a or event.key == K_LEFT:
            keys[2] = 0
        if event.key == K_d or event.key == K_RIGHT:
            keys[3] = 0


  screen.fill(DARK_GRAY)



  blockSize = 40  # Set the size of the grid block
  for x in range(len(matrix1)):
      for y in range(len(matrix1[0])):
          rect = pygame.Rect(x * 40, y * 40, blockSize, blockSize)
          if matrix1[y][x] == 1:
              pygame.draw.rect(screen, DARK_GRAY, rect, 0)
          else:
              pygame.draw.rect(screen, LIGHT_GRAY, rect, 0)

  if keys[0] == 1:
      plrY -= 1

  if keys[1] == 1:
      plrY += 1

  if keys[2] == 1:
      plrX -= 1

  if keys[3] == 1:
      plrX += 1

  screen.


  pygame.display.flip()

pygame.quit()



