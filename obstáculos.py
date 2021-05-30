#Importa a biblioteca random e o pygame, enquanto importa os dados do arquivo configuração.py
import random
import pygame
from configuração import *

#Cria a classe dos obstáculos
class Obstaculos(pygame.sprite.Sprite):

    #Define a função inicializadora da classe
    
    def __init__(self,posicao,vel_chão):

        # Inicialização dos sprites e coleta de imagem
        
        pygame.sprite.Sprite.__init__(self)
        
        #Carregando a imagem 
        
        self.image = pygame.image.load('imagens/pipe.png').convert_alpha()
        
        #Formando um retângulo através da imagem
        
        self.rect = self.image.get_rect()
        
        #Verifica se bateu no obstáculo
        
        self.acabou = False
        
        # Espaço mínimo entre os obstáculos
        
        self.gap = 120
        
        # Variação aleatória
        
        self.rand = random.randint(-50,90)

        # Velocidade do obstáculo é equivalente a do chão:
        
        self.vel = vel_chão
        
        # Posição dos sprites
       
        self.y = (HEIGHT/3) + self.rand
        
        #"if" que verifica a posição do obstáculo
        
        if posicao == 'topo':
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = [WIDTH, self.y]
        if posicao == 'baixo':
            self.rect.topleft = [WIDTH, self.y]
    
    # Método que atualiza a disposição dos obstáculos    
    
    def update(self):
        
        if self.acabou == False:
            
        # Deslocamento horizontal dos obstáculos 

            self.rect.x += self.vel
        
        # Remove os sprites que sumiram da tela
        
        if self.rect.right < 0:
            self.kill()
    
    # Método para parar a movimentação do jogo (para a movimentação dos obstáculos)
    
    def para(self):
        self.acabou = True
        
