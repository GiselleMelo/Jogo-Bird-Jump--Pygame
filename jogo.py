# Importa configurações

from configuração import *

# Classe que representa o jogo. Será chamada pelo arquivo main.

class Jogo:
    
###################################### Inicialização #################################################    
    
    def __init__(self):

        # Inicializando o pygame
        pygame.init()

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
        #configurando o estado como INICIAL.
        self.state = 'INICIAL'

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
        pygame.Surface.fill(self.window,(255,255,255))

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
    
    # Seleção de personagens
    def trans_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # mudança de estado; só ocorre se um personagem foi selecionado
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.jogador_selecionado != '':
                self.state = 'JOGANDO'
            # Escolhendo o personagem
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                self.jogador_selecionado = 'galinha'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                self.jogador_selecionado = 'verde'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                self.jogador_selecionado = 'amarelo'
    
    # Atualizando as informações no display
    def trans_draw(self):
         pygame.display.update()
         pygame.Surface.fill(self.window,(255,255,255))

######################################## JOGANDO ####################################################
#Nessa parte o jogo será iniciado para a interação com o jogador
    
    def jog_inicial(self):
        
        # Inicializando sprites/grupos
        self.bird = Bird(self.jogador_selecionado)
        self.all_pipes = pygame.sprite.Group()
        self.all_birds = pygame.sprite.Group()
        self.all_birds.add(self.bird)
        
        # Impede de segurar o botão para voar constantemente
        self.apertado = False
        
        # Posição e velocidade do chão
        self.ground_scroll = 0
        self.ground_vel = - 4
        
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
        
        