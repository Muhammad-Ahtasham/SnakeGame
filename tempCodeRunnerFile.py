gImg1 = pygame.image.load('snakeBG.jpg')
    #convert_alpha() helps to retain the game speed while bliting the game window again and again
    bgImg = pygame.transform.scale(bgImg1, (screenWidth, screenHeight))