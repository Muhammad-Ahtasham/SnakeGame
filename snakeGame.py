import random
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
velocityX = 0
velocityY = 0  
snakeSize = 10
fps = 30            #frames per second

#created food for the snake
foodX = random.randint(20, screenWidth/2)
foodY = random.randint(20, screenHeight/2)

# creating score
score = 0
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
def screenScore(text, color, x, y):
    screenText = font.render(text, True, color) # is ma  true is antialising --> high to low resolution convertion
    
    # blit is used to update it all on screen
    gameWindow.blit(screenText, [x, y]) 
while not exitGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitGame = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocityX = 10
                velocityY = 0
            if event.key == pygame.K_LEFT:
                velocityY = 0
                velocityX = -10
            if event.key == pygame.K_UP:
                velocityX = 0
                velocityY = -10
            if event.key == pygame.K_DOWN:
                velocityX = 0
                velocityY = 10
    
    snakeX = snakeX + velocityX
    snakeY = snakeY + velocityY
    if abs(snakeX-foodX)<6 and abs(snakeY-foodY)<6:
        score += 1
        
        foodX = random.randint(20, screenWidth/2)
        foodY = random.randint(20, screenHeight/2) 
        print('Score: ', score)


    gameWindow.fill(white)
    screenScore('Score: ' + str(score), red, 5, 5)
    pygame.draw.rect(gameWindow, black, [snakeX, snakeY, snakeSize, snakeSize])
    pygame.draw.rect(gameWindow, red, [foodX, foodY, snakeSize, snakeSize])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()