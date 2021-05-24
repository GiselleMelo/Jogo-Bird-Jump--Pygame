# Importa configurações

from config import *

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
                self.jog_inicial()
                while self.state == 'TRANSIÇÃO':
                    pass
                while self.state == 'JOGANDO':
                    self.jog_eventos()
                    self.jog_draw()
                    self.clock.tick(fps)
                self.fim_inicial()
                while self.state == 'FIM':
                    self.fim_eventos()
                    self.fim_draw()
                    self.clock.tick(fps)