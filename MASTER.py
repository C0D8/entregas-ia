from aigyminsper.search.SearchAlgorithms import BuscaLargura
from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aigyminsper.search.Graph import State
import copy

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


        if self.posicao_robo[0] < len(self.situacao)-1:
            sucessors.append(AspiradorPo("baixo",[self.posicao_robo[0]+1,self.posicao_robo[1]],self.situacao,self.quartos))
        if self.posicao_robo[0] >= 1 :
            sucessors.append(AspiradorPo("cima",[self.posicao_robo[0]-1,self.posicao_robo[1]],self.situacao,self.quartos))
        if self.posicao_robo[1] < len(self.situacao)-1:
            sucessors.append(AspiradorPo("dir",[self.posicao_robo[0],self.posicao_robo[1]+1],self.situacao,self.quartos))
        if self.posicao_robo[1] >= 1 :
            sucessors.append(AspiradorPo("esq",[self.posicao_robo[0],self.posicao_robo[1]-1],self.situacao,self.quartos))


        # limpar
        novo =  copy.deepcopy(self.situacao)    
        novo[self.posicao_robo[0]][self.posicao_robo[1]] = 0

        sucessors.append(AspiradorPo("NHAC",self.posicao_robo,novo,self.quartos))
        

        return sucessors

    def is_goal(self):
        if self.situacao == [[0 for i in range (10)] for j in range(10)]:
            return True
        return False 

    def cost(self):
        return 1

    def description(self):
        return "Implementa um aspirador de po para 2 quartos"

    def env(self):
        return self.operator


def main():

    vet = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 
0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    state = AspiradorPo('',[0,0],vet,[[0 for i in range (10)] for j in range(10)])
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()