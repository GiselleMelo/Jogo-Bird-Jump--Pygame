import pygame
from configuração import *
from jogo import *

###Criando a classe do jogador###

class Bird(pygame.sprite.Sprite):
    #método de inicialização
    def __init__(self,jogador):
        #inicia os sprites
        pygame.sprite.Sprite.__init__(self)
        #adicionando as imagens para projetar
        self.images = []
        #índice inicial da lista
        self.index = 0
        #adicionando o contador de pontos
        self.contador = 0
        # Jogadores
        if jogador == 'rosa':
            for num in range(1,3):
                #carrega a imagem do pássaro rosa
                img = pygame.image.load('bird/rosa_{0}.png'.format(num)).convert_alpha()
                img = pygame.transform.scale(img,(51,36))
                #adiciona a imagem
                self.images.append(img)
            #configura o pulo e a frequência 
            self.pulo = 10
            self.freq = freq - 200
        elif jogador == 'bege':
            for num in range(1,3):
                #carrega a imagem do pássaro bege
                img = pygame.image.load('bird/bege_{0}.png'.format(num)).convert_alpha()
                img = pygame.transform.scale(img,(51,36))
                self.images.append(img)
            #configura o pulo e a frequência dele 
            #note que é diferente do jogador rosa, ocasionando diferenças no jogo
            self.pulo = 8
            self.freq = freq
        #atualiza a imagem sempre que ela muda
        self.image = self.images[self.index]
        #gera um retângulo a partir da imagem
        self.rect = self.image.get_rect()
        #condições iniciais do pássaro
        self.rect.center = [90,b_ini]
        self.vel = 0
        #analisa se o pássaro pode pular
        self.pode_pular = True
        
        # Estado inicial do jogo, antes de começar voar
        self.voando = False