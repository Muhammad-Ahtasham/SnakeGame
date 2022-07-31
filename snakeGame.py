import random
from turtle import color
import pygame
pygame.init()

#colours
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
screenWidth = 1000
screenHeight = 600

gameWindow = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("NaganGame")
pygame.display.update()


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def screenScore(text, color, x, y):
    screenText = font.render(text, True, color) # is ma  true is antialising --> high to low resolution convertion
    
    # blit is used to update it all on screen
    gameWindow.blit(screenText, [x, y]) 

def plotSnake(gameWindow, color, snakeList, snakeSize):
    for x, y in snakeList:
        pygame.draw.rect(gameWindow, color, [x, y, snakeSize, snakeSize])

def welcome():
    exitGame = False
    while not exitGame:
        gameWindow.fill(black)
        screenScore("Welcome to SnakeFriendsAndRishtadar Game", white, 65, 200)
        screenScore("Press Space Bar to Start", white, 245, 280)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                exitGame = True
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_SPACE:
                    gameLoop()
        pygame.display.update()
        clock.tick(30)

def gameLoop():

    # creating score
    gameOver = False
    score = 0
    exitGame = False
    snakeX = 45
    snakeY = 55
    velocityX = 0
    velocityY = 0  
    snakeSize = 10
    fps = 30            #frames per second

    snakeList = []
    snakeLength = 1
    with open("highScore.txt", "r") as f:
        highScore =  f.read()
    #created food for the snake
    foodX = random.randint(20, screenWidth/2)
    foodY = random.randint(20, screenHeight/2)
    while not exitGame:    
        if gameOver:
            with open("highScore.txt", "w") as f:
                f.write(str(highScore)) 
            gameWindow.fill(white)
            screenScore("Game Over! Press Enter to Continue", red, screenWidth/7, screenHeight/2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitGame = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitGame = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocityX = 5
                        velocityY = 0
                    if event.key == pygame.K_LEFT:
                        velocityY = 0
                        velocityX = -5
                    if event.key == pygame.K_UP:
                        velocityX = 0
                        velocityY = -5
                    if event.key == pygame.K_DOWN:
                        velocityX = 0
                        velocityY = 5
                    if event.key == pygame.K_q:
                        score += 4
            
            snakeX = snakeX + velocityX
            snakeY = snakeY + velocityY
            if abs(snakeX-foodX)<5 and abs(snakeY-foodY)<4:
                score += 1
                foodX = random.randint(20, screenWidth/2)
                foodY = random.randint(20, screenHeight/2) 
                snakeLength += 5
                if score>int(highScore):
                    highScore = score
                    
            gameWindow.fill(white)
            screenScore('Score: ' + str(score)+ "             HighScore: "+ str(highScore), red, 5, 5)
            # pygame.draw.rect(gameWindow, black, [snakeX, snakeY, snakeSize, snakeSize])
            pygame.draw.rect(gameWindow, red, [foodX, foodY, snakeSize, snakeSize])

            head = []
            head.append(snakeX)
            head.append(snakeY)
            snakeList.append(head)
            if len(snakeList) >snakeLength:
                del snakeList[0]

            if snakeX <0 or snakeX>screenWidth or snakeY<0 or snakeY>screenHeight:
                gameOver = True
            if head in snakeList[:-1]:
                gameOver = True
            plotSnake(gameWindow, black, snakeList, snakeSize)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()