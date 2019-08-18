import pygame
#Yasin Güneş

pygame.init()
pygame.display.set_caption('Oyun')

fps = 60
topX, topY = 400, 300
raket1X, raket1X2 = 50, 50  #Başlangıç noktası
raket1Y, raket1Y2 = 50, 200 #Bitiş noktası
ekr_boyut = (899, 600)

pencere = pygame.display.set_mode((ekr_boyut))
sonpencere = pygame.display.set_mode((ekr_boyut))
font = pygame.font.SysFont("Helvatica",100)
font2 = pygame.font.SysFont("Helvatica",50)

rekor = 0
ölüm = 0

gameOver = False


yonx, yony = 1, 1

clock = pygame.time.Clock()
pygame.mouse.set_visible(0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    clock.tick(fps)
    pencere.fill((0, 0, 0))


    if not gameOver:
        pygame.draw.line(pencere, (250, 250, 250), (810, 0), (810, 600), 1)

        sayaç = font.render(str(rekor), 1, (255, 255, 255), (0, 0, 0))

        top = pygame.draw.circle(pencere, (255, 255, 255), (topX, topY), 15)
        topX += 5 * yonx
        topY += 5 * yony
        if topX > 790 or topX < 20 or topY > raket1Y and topY < raket1Y2 and topX - 10 == raket1X:
            yonx *= -1
            if topX > 790:
                rekor += 1
            if topX - 16 < 0:
                gameOver = True
                pencere.fill((0, 0, 0))
                ölüm_font = font2.render("Oyun Bitti", 1, (255, 255, 255), (0, 0, 0))
                pencere.blit(ölüm_font, ((ekr_boyut[0] / 2) - ölüm_font.get_size()[1], ekr_boyut[1] / 2))
                pygame.display.update()
                pygame.time.wait(2000)
                pygame.quit()


        if topY + 19 > 600 or topY - 19 < 0:
            yony *= -1

        raket1 = pygame.draw.line(pencere, (255, 255, 255), (raket1X, raket1Y ), (raket1X2, raket1Y2), 4 )
        raket1Y, raket1Y2 = pygame.mouse.get_pos()[1], pygame.mouse.get_pos()[1] + 150


        pencere.blit(sayaç, (820,300))
        pygame.display.update()
