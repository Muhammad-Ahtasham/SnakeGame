from pickle import TRUE
from numpy import true_divide
import pygame
pygame.init()

#colours
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
screenWidth = 900
screenHeight = 600

gameWindow = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("SnakeWithAtiii")
pygame.display.update()

exitGame = False
gameOver = False
snakeX = 45
snakeY = 55
snakeSize = 10


while not exitGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitGame = TRUE
    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, black, [snakeX, snakeY, snakeSize, snakeSize])
    pygame.display.update()

pygame.quit()
quit()