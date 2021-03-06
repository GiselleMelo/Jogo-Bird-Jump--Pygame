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
        #adicionando as imagens após colisões
        self.imagesres =[]
        #índice inicial da lista
        self.index = 0
        #adicionando o contador de pontos
        self.contador = 0
        # Jogadores
        if jogador == 'galinha':
            self.dimensao = (48,30)
            for num in range(1,5):
                #carrega a imagem do pássaro rosa
                img = pygame.image.load('bird/galinha{0}.png'.format(num)).convert_alpha()
                img = pygame.transform.scale(img,self.dimensao)
                #adiciona a imagem
                self.images.append(img)
            #configura o pulo e a frequência 
            self.pulo = 10
            self.freq = freq - 25
        elif jogador == 'verde':
            self.dimensao = (51,36)
            for num in range(1,5):
                #carrega a imagem do pássaro bege
                img = pygame.image.load('bird/verde ({0}).png'.format(num)).convert_alpha()
                img = pygame.transform.scale(img,self.dimensao)
                self.images.append(img)
            #configura o pulo e a frequência 
            self.pulo = 8
            self.freq = freq 
        elif jogador == 'amarelo':
            self.dimensao = (30,20)
            for num in range(1,5):
                img = pygame.image.load('bird/amarelo1 ({0}).png'.format(num)).convert_alpha()
                img = pygame.transform.scale(img,self.dimensao)
                self.images.append(img)
            #configura o pulo e a frequência dele 
            #note que é diferente do jogador rosa, ocasionando diferenças no jogo
            self.pulo = 9
            self.freq = freq + 70
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
    
    # Método que atualiza a posição do pássaro
    def update(self):
        
        # Se o pássaro está fora do estado inicial
        if self.voando:

            # Efeito da gravidade
            self.vel += 0.5
        
            # Limitando a velocidade mínima e máxima
            if self.vel > 8:
                self.vel = 8
            if self.vel < -self.pulo:
                self.vel = -self.pulo
            
            
        # Caso o passaro não caia no chão
        
        if self.rect.bottom < g_HEIGHT:

        # Atualiza a posição no eixo y
            self.rect.y += int(self.vel)

        # Animação:
            
            # Contador para passar sprite da animação
            self.contador += 1
            # Limite do contador antes de trocar
            flap_cooldown = 6
        
            if self.contador > flap_cooldown:
                self.contador = 0
                # Aumenta o índice da lista images para alterar a imagem
                self.index += 1
                # Volta para o índice 0 quando acabar a lista
                if self.index >= len(self.images):
                    self.index = 0

            self.image = self.images[self.index]
           # Limita o alcance do jogador:
            if self.rect.top < 0:
                self.rect.top = 0
                self.vel = 0
            
        # Rotação

            # Direção da rotação depende do sentido da velocidade 
            self.image = pygame.transform.rotate(self.images[self.index],self.vel * -3)
        else:
            # No fim do jogo o pássaro cai em 90 graus
            self.image = pygame.transform.rotate(self.images[self.index],-90)
            
        
    def pula(self):
        
        # Função do pulo. Não funciona quando jogador bate no cano ou no chão.
        if self.pode_pular == True:
            self.vel -= self.pulo

    #muda a lista de imagens para a dos pássaros pós colisão com o cano
    def troca(self):
        self.index = 0
        self.images = self.imagesres