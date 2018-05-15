import pygame

pygame.init()

pygame.display.set_caption("test")
pygame.display.set_mode((500, 500))
pygame.mixer.init()

end = True
while end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_q:
                  pygame.mixer.Sound("eat1.ogg").play()
        if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_w:
                  pygame.mixer.Sound("eat2.ogg").play()


