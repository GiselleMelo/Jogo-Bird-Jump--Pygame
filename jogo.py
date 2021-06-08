# Importa configurações
import pygame
from configuração import *
import sys
import random
from passaro import Bird
from obstáculos import Pipe


# Classe que representa o jogo. Será chamada pelo arquivo main.

class Jogo:
    
###################################### Inicialização #################################################    
    
    def __init__(self):

        # Inicializando o pygame
        pygame.init()
        
        # Inicializando música
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.5)

        # Configurando a tela
        self.window = pygame.display.set_mode((WIDTH,HEIGHT))

        # Atribui o estado inicial do jogo, detalhado na estrutura
        self.state = 'INICIAL'

        # Carrega os assets
        self.assets = load_assets()

        # Variável que condiciona o loop de gameplay 
        self.game = True

        # Configura a frequência que o código é rodado
        self.clock = pygame.time.Clock()
        
        # Variável que condiciona o loop principal
        self.rodando = True

        # Varíavel que representa o high score
        self.highscore = 0

###################################### Estrutura de um jogo ##########################################
    
    # Método que roda o jogo
    # Chama outros métodos, os quais alteram o estado do jogo

    # Cada estado apresentado tem 3 métodos: ini, eventos e draw:
        
        # O ini atribui as condições iniciais e encapsula as classes

        # O eventos lida com interações do usuário e busca gatilhos de mudança de estado

        # O draw distribui as informações para o display


    # Os estados são:
    
        # INICIAL: relativo a tela inicial; não é repetido no loop de gameplay
        # TRANSICAO: menu de escolha de personagem + mostrador de nível
        # JOGANDO: O jogo em si
        # FIM: Tela final; tanto de vitória quanto derrota   

    def run(self):
        # Loop principal: 
        while self.rodando:
            self.ini_inicial()
            # Loop do menu principal
            while self.state == 'INICIAL':
                self.ini_eventos()
                self.ini_draw()
                self.clock.tick(fps)
            # Loop de gameplay
            while self.game:
                self.trans_ini()
                while self.state == 'TRANSIÇÃO':
                    self.trans_eventos()
                    self.trans_draw()
                    self.clock.tick(fps)
                self.jog_inicial()
                while self.state == 'JOGANDO':
                    self.jog_eventos()
                    self.jog_draw()
                    self.clock.tick(fps)
                self.fim_inicial()
                while self.state == 'FIM':
                    self.fim_eventos()
                    self.fim_draw()
                    self.clock.tick(fps)

########################################### INICIAL ##################################################
    # Método que configura a tela inicial
    # Ela tem fins estéticos; para apresentar o jogo 

    def ini_inicial(self):
        #reinicia o loop de game play caso o jogador volte para o inicial 
        self.game = True
        #configurando o estado como INICIAL.
        self.state = 'INICIAL'
        # Carregando música de fundo
        pygame.mixer.music.load('sons/som-inicial.mp3')
        pygame.mixer.music.play()

    #Método que define os eventos no estado inicial.
    #A partir da tecla que a pessoa seleciona há uma iteração com o 'eventos'.
    def ini_eventos(self):
        #Analisa cada evento
        for event in pygame.event.get():
            #se for o caso de saída, ele sai:
            if event.type == pygame.QUIT:
                pygame.quit()
                #garantindo que saiu do jogo
                sys.exit()
            #Verifica se o botão espaço foi apertado
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'TRANSIÇÃO'
                
    #Método que vai atualizar as informações recebidas no display
    def ini_draw(self):
        pygame.display.update()
        self.window.blit(self.assets['ini'],(0,0))
        draw_texto(self.window,'Bird Jump',self.assets['fonte3'],(255,255,0),(150,75))
        draw_texto(self.window,"Pressione espaço para começar!",self.assets['fonte2'],(255,255,255),(95,400))
        self.window.blit(self.assets['verde'],(350,250))
        self.window.blit(self.assets['galinha'],(50,250))
        self.window.blit(self.assets['amarelo'],(200,250))
##################################### TRANSIÇÃO ####################################################
    #Método que apresenta a seleção dos personagens
    # A princípio foram idealizados três personagens: a galinha, o verde, e o amarelo. 
    # os quais serão escolhido se selecionado a letra 'c' ou 'r'  ou 'a',  respectivamente.
    
    # Condições iniciais
    def trans_ini(self):
        # Inicializa o jogador como vazio, o que permite a mudança de personagens
        self.jogador_selecionado = ''
        # Nível é inicializado
        self.level = 1
        # Váriavel auxiliar para a mudança de tela
        self.muda_tela = False
        # Carrega música de fundo
        pygame.mixer.music.load('sons/som-transição.mp3')
        pygame.mixer.music.play()
    
    # Seleção de personagens
    def trans_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mudança de tela
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.muda_tela == False:
                self.muda_tela = True
            # mudança de estado; só ocorre se um personagem foi selecionado
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.jogador_selecionado != '' and self.muda_tela:
                self.state = 'JOGANDO'
            # Escolhendo o personagem
            if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                self.jogador_selecionado = 'galinha'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
                self.jogador_selecionado = 'verde'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                self.jogador_selecionado = 'amarelo'
    
    # Atualizando as informações no display
    def trans_draw(self):
         pygame.display.update()
         # Primeira tela da transição
         if self.muda_tela == False:
            self.window.blit(self.assets['trans1'],(0,0))
            draw_texto(self.window,'Como jogar:', self.assets['fonte3'], (0,0,0), (50,50))
            draw_texto(self.window,'Pule para desviar dos canos!', self.assets['fonte2'], (0,0,0), (25,150))
            draw_texto(self.window,'Aperte "espaço" para pular', self.assets['fonte2'], (0,0,0), (25,220))
            draw_texto(self.window,'Aperte "M" para remover a música', self.assets['fonte2'], (0,0,0), (25,280))
            draw_texto(self.window,'A dificuldade aumenta a cada 5 canos!', self.assets['fonte2'], (0,0,0), (25,340))
            draw_texto(self.window,'Para maior conforto, o pássaro começará parado', self.assets['fonte2'], (0,0,0), (25,400))
            draw_texto(self.window,'Personagens mudam as condições do jogo', self.assets['fonte2'], (0,0,0), (25,460))
            draw_texto(self.window,'Aperte "espaço" para continuar', self.assets['fonte2'], (0,0,0), (160,550))
        # Segunda tela da transição
         else:
             self.window.blit(self.assets['trans2'],(0,0))
             draw_texto(self.window,'Seleção de pássaro', self.assets['fonte3'], (0,0,0), (40,50))
             draw_texto(self.window,'Aperte "G"', self.assets['fonte2'], (0,0,0), (50,350))
             draw_texto(self.window,'Aperte "V"', self.assets['fonte2'], (0,0,0), (350,350))
             draw_texto(self.window,'Aperte "A"', self.assets['fonte2'], (0,0,0), (190,400))
             draw_texto(self.window,'Aperte espaço para continuar', self.assets['fonte2'], (0,0,0), (110,500))
             self.window.blit(self.assets['galinha'],(50,250))
             self.window.blit(self.assets['verde'],(350,250))
             self.window.blit(self.assets['amarelo'],(200,250))

######################################## JOGANDO ####################################################
#Nessa parte o jogo será iniciado para a interação com o jogador

    def jog_inicial(self):
        #alterando para a música do jogo
        pygame.mixer.music.load('sons/som-jogo.mp3') 
        pygame.mixer.music.play()
        # Inicializando sprites/grupos
        self.bird = Bird(self.jogador_selecionado)
        self.all_pipes = pygame.sprite.Group()
        self.all_birds = pygame.sprite.Group()
        self.all_birds.add(self.bird)
        # Escolhe um background aleatório da lista
        self.bg = random.choice(self.assets['bg'])
        # Depois de escolhida, é removida da lista
        self.assets['bg'].remove(self.bg)
        # Se não restar mais imagens, reinicia
        if len(self.assets['bg']) == 0:
            self.assets = load_assets()
        
        # Impede de segurar o botão para voar constantemente
        self.apertado = False
        
        # Posição e velocidade do chão
        self.ground_scroll = 0
        self.ground_vel = - 3
        
        # Impede a movimentação do chão e a criação de canos
        self.bateu = False
        self.last_pipe = pygame.time.get_ticks()

        # Impede while da condição de game over rodar o timer de novo:
        self.acabou = False 
        
        # Variáveis para formar o placar. Self.passou verifica se o pássaro está dentro do cano, para evitar contar mais de um ponto por cano
        self.score = 0
        self.passou = False


        # Variável que auxilia a passagem de nível
        self.momento_passa_nível = pygame.time.get_ticks()
        self.passa_nível = True
    
        #loop que adiciona as imagens de colisão
        for i in range(1,3):
            img = pygame.image.load('bird/{0}_bate{1}.png'.format(self.jogador_selecionado,i)).convert_alpha()
            img = pygame.transform.scale(img,self.bird.dimensao)
            self.bird.imagesres.append(img)
    

    def jog_eventos(self):
        
        # Novos canos:

        #armazenando o tempo que está passando 
        now = pygame.time.get_ticks()

        #implementando as condições para gerar novos canos
        if now - self.last_pipe > self.bird.freq and self.bird.voando == True and self.bateu == False:
            self.last_pipe = now
            baixo = Pipe('baixo',self.ground_vel)
            cima = Pipe('topo',self.ground_vel)
            #garantindo que exista um espaço fixo entre os canos
            baixo.rect.top = cima.rect.bottom + baixo.gap
            #adicionando os canos:
            self.all_pipes.add(baixo)
            self.all_pipes.add(cima)
            
        
        # Rolamento do chão 
        #confere se o jogador bateu
        if self.bateu == False:
            self.ground_scroll += self.ground_vel
            #recoloca o chão dando o efeito de continuidade
            if abs(self.ground_scroll) > 35:
                self.ground_scroll = 0
            
        # Condição de game over:
        #checa se há colisão entre os sprites (pássaro e cano)
        hit =  pygame.sprite.groupcollide(self.all_birds,self.all_pipes,False,False)
        
        #checa se ele cai no chão ou bate no cano
        if self.bird.rect.bottom >= g_HEIGHT or hit:
            #percorre a lista de canos e faz todos eles pararem.
            for sprite in self.all_pipes.sprites():
                sprite.para()
            #atualiza as condições
            self.bateu = True
            self.bird.pode_pular = False
            self.ground_vel = 0
            #garantindo que o self.momento não rode de novo
            if self.acabou == False:
                self.acabou = True
                #adicionando o som
                self.assets['morte'].play()
                #mudança para as imagens após a colisão
                self.bird.troca()
                #guardando o momento
                self.momento = pygame.time.get_ticks()
            else:    
                #checa se passou dois segundo após o self.momento para dar a condição de fim.
                if (now - self.momento > 2000):
                    self.state = "FIM"

        # Interações com o jogador
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Interação do pulo
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.apertado == False:
                self.bird.pula()
                self.apertado = True
            # Impede o jogador de segurar o botão para pular
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                self.apertado = False
            # Inicia o jogo (movimento do cano, pássaro, etc)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.bird.voando == False:
                self.bird.voando = True
            #caso o jogador queira tirar o som de fundo, por questão de comodidade
            #os efeitos sonoros irão continuar
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                pygame.mixer.music.stop()
            
                
        # Aumentar o placar:
        
        # Se passa pelo lado esquerdo --> entrou vira verdadeiro. Isso permite que só seja contabilizado um ponto por cano:

        # Checa os canos existentes    
        if self.all_pipes.sprites() != []:
            # verifica se entrou no cano
            if self.bird.rect.left > self.all_pipes.sprites()[0].rect.left and self.bird.rect.right < self.all_pipes.sprites()[0].rect.right:
                # variável auxiliar
                self.passou = True
            # verifica se saiu do cano
            if self.bird.rect.left > self.all_pipes.sprites()[0].rect.right and self.passou == True:
                # Toca som
                self.assets['cano'].set_volume(0.4)
                self.assets['cano'].play()
                self.passou = False
                # adiciona um ponto ao placar
                self.score += 1
            

        # Mudando de nível:
        
        # Verifica se o placar é múltiplo de 5 e diferente de 0
        if self.score % 5 == 0 and self.score != 0:
            # self.passa nível garante que o nível seja aumentado em apenas 1
            if self.passa_nível:
                self.passa_nível = False 
                self.level += 1
                # Toca som de fase
                self.assets['fase'].set_volume(0.4)
                self.assets['fase'].play()
                # guarda o momento
                self.momento_passa_nível = pygame.time.get_ticks()
                # Aumenta a velocidade dos canos
                self.ground_vel += - 1
            # Espera 3 segundos para permitir passar outro nível
            elif now - self.momento_passa_nível >= 3000:
                self.passa_nível = True
    
    #Método que exibe na tela 
    def jog_draw(self):
        # Desenho dos sprites e background
        pygame.display.update()
        self.window.blit(self.bg,(0,0))
        self.all_birds.draw(self.window)
        self.all_birds.update()
        self.all_pipes.draw(self.window)
        self.all_pipes.update()
        self.window.blit(self.assets['ground'],(self.ground_scroll,g_HEIGHT))
        #desenhando placar e nível 
        draw_texto(self.window,str(self.score),self.assets['fonte'],(255,255,255),(225,20))
        draw_texto(self.window, str('level {0}'.format(self.level)), self.assets['fonte2'], (255,255,255), (15,20))
        
########################################### FIM ######################################################
    
    def fim_inicial(self):
        # Carregando música de fundo:
        pygame.mixer.music.load('sons/som-final.mp3') 
        pygame.mixer.music.play()
        if self.score > self.highscore:
            self.highscore = self.score   

    #Método que define o fim de eventos
    def fim_eventos(self):
        #finaliza cada um 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'TRANSIÇÃO'
            #m volta pro menu
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                self.game = False
                self.highscore=0
                self.state = 'ACABOU'

    #fim draw aparece aqui
    def fim_draw(self):
        pygame.display.update()
        self.window.blit(self.assets['fim'],(0,0))
        draw_texto(self.window,'Você perdeu!',self.assets['fonte3'],(255,255,255),(100,50))
        draw_texto(self.window,'Que deselegante!', self.assets['fonte3'], (0,0,0), (65,100))
        draw_texto(self.window,"Placar: {0}".format(self.score),self.assets['fonte3'],(255,255,255),(150,200))
        draw_texto(self.window,"High score: {0}".format(self.highscore),self.assets['fonte3'],(255,255,255),(110,280))
        draw_texto(self.window,"Aperte espaço para continuar",self.assets['fonte2'],(255,255,255),(110,380))
        draw_texto(self.window,'ou "M" para voltar a tela de início',self.assets['fonte2'],(255,255,255),(110,430))