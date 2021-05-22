import pygame
from pygame.locals import *

# Dimensões da tela:
WIDTH = 500
HEIGHT = 600

# Posição do chão:

g_HEIGHT = 473
    
# FPS:
fps = 30

# Altura inicial do pássaro:
b_ini = (HEIGHT/2) - 100

#Função que inicia os assets(será chamada pela classe do jogo)
def load_assets():
    assets = {}
    assets['bg'] = pygame.image.load('').convert()
    #transformando para a escala do jogo
    assets['bg'] = pygame.transform.scale(assets['bg'],(WIDTH,HEIGHT))
    assets['ground'] = pygame.image.load('').convert()
    assets['fonte'] = pygame.font.SysFont('Bauhaus 93',40)
    assets['musica'] = 'musica'
    assets['flap'] = 'barulho'
    return assets 