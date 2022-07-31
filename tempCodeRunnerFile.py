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
            
            snakeX = snakeX + velocityX
            snakeY = snakeY + velocityY
            if abs(snakeX-foodX)<6 and abs(snakeY-foodY)<6:
                score += 1
                foodX = random.randint(20, screenWidth/2)
                foodY = random.randint(20, screenHeight/2) 
                snakeLength += 5
                

            gameWindow.fill(white)
            screenScore('Score: ' + str(score), red, 5, 5)
            # pygame.draw.rect(gameWindow, black, [snakeX, snakeY, snakeSize, snakeSize])
            pygame.draw.rect(gameWindow, red, [foodX, foodY, snakeSize, snakeSize])

            head = []
            head.append(snakeX)
            head.append(snakeY)
            snakeList.append(head)
            if len(snakeList) >snakeLength:
                del snakeList[0]

            if snakeX <0 or snakeX>screenWidth or snakeY<0 or snakeY>screenHeight:
                print("game vover")
            plotSnake(gameWindow, black, snakeList, snakeSize)