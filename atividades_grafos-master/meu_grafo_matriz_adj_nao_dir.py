from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *
#from bibgrafo.aresta import Aresta

class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto (set) de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um conjunto (set) com os pares de vértices não adjacentes
        '''

        naoadjecentes = set()

        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                vertice1 = self.vertices[i].rotulo
                vertice2 = self.vertices[j].rotulo

                if not self.matriz[i][j] and vertice1 != vertice2:
                    if vertice1 > vertice2:
                        naoadjecentes.add((vertice2+'-'+vertice1))
                    else:
                        naoadjecentes.add((vertice1+'-'+vertice2))

        return(naoadjecentes)

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''


        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                vertice1 = self.vertices[i].rotulo
                vertice2 = self.vertices[j].rotulo

                if self.matriz[i][j] and vertice1 == vertice2:
                    return True

        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''

        vertice1 = V
        contalaço = 0
        grauscontados = []

        if not self.existe_rotulo_vertice(vertice1):
            raise VerticeInvalidoError


        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                vertice2a = self.vertices[i].rotulo
                vertice2b = self.vertices[j].rotulo
                if self.matriz[i][j] and (vertice1 == vertice2a or vertice1 == vertice2b):
                    #print(self.matriz[i][j])

                    for x in range( len( list(self.matriz[i][j].keys()) ) ):

                        if list(self.matriz[i][j].keys())[x] not in grauscontados:

                            grauscontados.append(list(self.matriz[i][j].keys())[x])
                            if self.matriz[i][j] and (vertice2a == vertice1 and vertice2b == vertice1):
                                contalaço = contalaço + 1


        #print(grauscontados)
        #print(contalaço)

        return (len(grauscontados)+contalaço)

        #if contadorgrau < 0:
            #contadorgrau = 0

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                vertice1 = self.vertices[i].rotulo
                vertice2 = self.vertices[j].rotulo

                if self.matriz[i][j] and len(list(self.matriz[i][j])) > 1:
                    print(self.matriz[i][j])
                    for z1 in range(len(self.matriz[i][j])):
                        for z2 in range(len(self.matriz[i][j])):
                            if z1 != z2 and list(self.matriz[i][j].values())[z1] == list(self.matriz[i][j].values())[z2]:
                                return True

        return False
    def arestas_sobre_vertice(self, V):
        '''
        Provê um conjunto (set) que contém os rótulos das arestas que
        incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Um conjunto com os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''

        vertice1 = V
        grauscontados = []

        if not self.existe_rotulo_vertice(vertice1):
            raise VerticeInvalidoError

        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                vertice2a = self.vertices[i].rotulo
                vertice2b = self.vertices[j].rotulo
                if self.matriz[i][j] and (vertice1 == vertice2a or vertice1 == vertice2b):
                    # print(self.matriz[i][j])

                    for x in range(len(list(self.matriz[i][j].keys()))):

                        if list(self.matriz[i][j].keys())[x] not in grauscontados:
                            grauscontados.append(list(self.matriz[i][j].keys())[x])

        return grauscontados

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                vertice1 = self.vertices[i].rotulo
                vertice2 = self.vertices[j].rotulo

                if (self.matriz[i][j] == {} and not vertice1 == vertice2) or self.ha_paralelas() or self.ha_laco():
                    print(self.matriz)
                    return False
        return True
