import pygame
from pygame.locals import *

# Dimensões da tela:
WIDTH = 500
HEIGHT = 600

# Posição do chão:

g_HEIGHT = 473
    
# FPS:
fps = 60

#frequência de referência para a formação de canos
freq=1500

# Altura inicial do pássaro:
b_ini = (HEIGHT/2) - 100

#Função que inicia os assets(será chamada pela classe do jogo)
def load_assets():
    assets = {}
    #importando as imagens para as telas
    #inicio
    assets['ini'] = pygame.image.load('imagens/inicio.png').convert()
    assets['ini'] =  pygame.transform.scale(assets['ini'],(WIDTH,HEIGHT))
    #primeira tela de transição
    assets['trans1'] = pygame.image.load('imagens/transicao.jpg').convert()
    assets['trans1'] =  pygame.transform.scale(assets['trans1'],(WIDTH,HEIGHT))
    #segunda tela de transição que será implementada posteriormente, onde ficará a escolha dos personagens
    #assets['trans2'] = pygame.image.load('imagens/transicao2.jpg').convert()
    #assets['trans2'] =  pygame.transform.scale(assets['trans2'],(WIDTH,HEIGHT))
    #tela final 
    assets['fim'] = pygame.image.load('imagens/final.png').convert()
    assets['fim'] =  pygame.transform.scale(assets['fim'],(WIDTH,HEIGHT))
    #tela inicial 
    assets['verde'] = pygame.image.load('bird/verde (2).png').convert_alpha()
    assets['verde'] = pygame.transform.scale(assets['verde'], (71,56))
    assets['verde'] = pygame.transform.rotate(assets['verde'], 30)
    assets['galinha'] = pygame.image.load('bird/galinha1.png').convert_alpha()
    assets['galinha'] = pygame.transform.scale(assets['galinha'], (68,50))
    assets['galinha'] = pygame.transform.rotate(assets['galinha'], 30)
    assets['amarelo'] = pygame.image.load('bird/amarelo1 (1).png').convert_alpha()
    assets['amarelo'] = pygame.transform.scale(assets['amarelo'], (50,45))
    assets['amarelo'] = pygame.transform.rotate(assets['amarelo'], 30)
    
    assets['bg'] = []
    #carregando os backgrounds png na lista
    for i in range(1,5):
        img = pygame.image.load('imagens/bg_{0}.png'.format(i)).convert()
        #transformando a escala da imagem
        img =  pygame.transform.scale(img,(WIDTH,HEIGHT))
        assets['bg'].append(img)
    #carregando o background jpg na lista
    img2 = pygame.image.load('imagens/background.jpg').convert()
    #transformando a escala da imagem
    img2 = pygame.transform.scale(img2,(WIDTH,HEIGHT))
    assets['bg'].append(img2)
    assets['ground'] = pygame.image.load('imagens/ground.png').convert()
    # Importanto fontes
    assets['fonte'] = pygame.font.SysFont('Bauhaus 93',40)
    assets['fonte2'] = pygame.font.SysFont('Bauhaus 93',20)
    assets['fonte3'] = pygame.font.SysFont('Bauhaus 93',47)
    # Importando sons:
    assets['morte'] = pygame.mixer.Sound('sons/som-morte.mp3')
    assets['fase'] = pygame.mixer.Sound('sons/som-fases.mp3')
    assets['cano'] = pygame.mixer.Sound('sons/som-cano.mp3')
    return assets 

# Função auxiliadora para exibir texto:
def draw_texto(window,texto,fonte,cor,pos):
    tex = fonte.render(texto,True,cor)
    window.blit(tex,pos)