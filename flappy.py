import pygame
from pygame.locals import *

#criando o display
SCREEN_WIDTH = 626 #largura da tela
SCREEN_HEIGHT = 417 #altura da tela


#iniciando
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#introduzindo o plano de fundo
BACKGROUND1 = pygame.image.load('background1.jpg')
#transformando a imagem original para o tamanho do jogo (625x417)
BACKGROUND1 = pygame.transform.scale (BACKGROUND1, (SCREEN_WIDTH,SCREEN_HEIGHT))

#Laço principal o qual fica se repetindo durante o jogo
while True:
    #chamaremos de event as atitudes tomadas pelo jogador
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    #Colocando o plano de fundo para o primeiro frame
    screen.blit(BACKGROUND1,(0,0))

    #vendo o que a atitude do jogador influenciou
    pygame.display.update()