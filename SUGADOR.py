from aigyminsper.search.SearchAlgorithms import BuscaLargura
from aigyminsper.search.Graph import State

class AspiradorPo(State):

    def __init__(self, op, posicao, sit, quartos):
        self.operator = op
        # DIR; ESQ
        self.posicao_robo = posicao #[0, 0]
        # LIMPO; SUJO  ; 0, 1;
        self.situacao = sit         #[[0,0],[0,0]]
        # LIMPO; SUJO
        self.quartos = quartos     #[[0,0],
                                #   [0,0]]

    def sucessors(self):
        sucessors = []

        # esq cima

        if self.posicao_robo == [0,0]: 
            sucessors.append(AspiradorPo("dir-cima",[0,1],self.situacao,self.quartos))
        if self.posicao_robo == [0,0]:    
            sucessors.append(AspiradorPo("esq-baixo",[1,0],self.situacao,self.quartos))
            
        # dir cima
        if self.posicao_robo == [0,1]: 
            sucessors.append(AspiradorPo("dir-baixo",[1,1],self.situacao,self.quartos))
        if self.posicao_robo == [0,1]: 
            sucessors.append(AspiradorPo("esq-cima",[0,0],self.situacao,self.quartos))
        # esq baixo
        if self.posicao_robo == [1,0]: 
            sucessors.append(AspiradorPo("esq-cima",[0,0],self.situacao,self.quartos))
        if self.posicao_robo == [1,0]: 
            sucessors.append(AspiradorPo("dir-baixo",[1,1],self.situacao,self.quartos))
        # dir baixo
        if self.posicao_robo == [1,1]: 
            sucessors.append(AspiradorPo("dir-cima",[0,1],self.situacao,self.quartos))
        if self.posicao_robo == [1,1]: 
            sucessors.append(AspiradorPo("esq-baixo",[1,0],self.situacao,self.quartos))


        # limpar
        if self.posicao_robo == [0,0]:
            sucessors.append(AspiradorPo("SUGANDO",self.posicao_robo,[[0,self.situacao[0][1]], [self.situacao[1][0],self.situacao[1][1]]],self.quartos))
        if self.posicao_robo == [1,0]:
            sucessors.append(AspiradorPo("SUGANDO",self.posicao_robo,[[self.situacao[0][0],self.situacao[0][1]], [0,self.situacao[1][1]]],self.quartos))
        if self.posicao_robo == [0,1]:
            sucessors.append(AspiradorPo("SUGANDO",self.posicao_robo,[[self.situacao[0][0],0], [self.situacao[1][0],self.situacao[1][1]]],self.quartos))
        if self.posicao_robo == [1,1]:
            sucessors.append(AspiradorPo("SUGANDO",self.posicao_robo,[[self.situacao[0][0],self.situacao[0][1]], [self.situacao[1][0],0]],self.quartos))
        

        return sucessors

    def is_goal(self):
        if self.situacao == [[0,0], [0,0]]:
            return True
        return False 

    def cost(self):
        return 1

    def description(self):
        return "Implementa um aspirador de po para 2 quartos"

    def env(self):
        return self.operator


def main():
    state = AspiradorPo('',[0,0],[[0,1],[1,0]],[[0,0],[0,0]])
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()