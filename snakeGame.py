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
fps = 30            #frames per second


clock = pygame.time.Clock()

while not exitGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitGame = TRUE
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snakeX = snakeX+10
            if event.key == pygame.K_LEFT:
                snakeX = snakeX-10
            if event.key == pygame.K_UP:
                snakeY = snakeY-10
            if event.key == pygame.K_DOWN:
                snakeY = snakeY+10



    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, black, [snakeX, snakeY, snakeSize, snakeSize])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()