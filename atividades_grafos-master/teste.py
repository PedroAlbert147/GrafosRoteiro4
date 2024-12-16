
#from bibgrafo.grafo_lista_adj_nao_dir import GrafoListaAdjacenciaNaoDirecionado

from bibgrafo.aresta import Aresta
from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.vertice import Vertice


#JCEPMTZ

j = Vertice("J")
c = Vertice("C")
e = Vertice("E")
p = Vertice("P")
m = Vertice("M")
t = Vertice("T")
z = Vertice("Z")

#g(a1) = JC, g(a2) = CE, g(a3) = CE, g(a4) = CP, g(a5) = CP, g(a6) = CM, g(a7) = CT, g(a8) = MT, g(a9) = TZ

a1 = Aresta("a1",j,c)
a2 = Aresta("a2",c,e)
a3 = Aresta("a3",c,e)
a4 = Aresta("a4",c,p)
a5 = Aresta("a5",c,p)
a6 = Aresta("a6",c,m)
a7 = Aresta("a7",c,t)
a8 = Aresta("a8",m,t)
a9 = Aresta("a9",t,z)

paraiba = GrafoMatrizAdjacenciaNaoDirecionado([j,c,e,p,m,t,z])
'''
paraiba.adiciona_vertice(j)
paraiba.adiciona_vertice(c)
paraiba.adiciona_vertice(e)
paraiba.adiciona_vertice(p)
paraiba.adiciona_vertice(m)
paraiba.adiciona_vertice(t)
paraiba.adiciona_vertice(z)
'''

paraiba.adiciona_aresta(a1)
paraiba.adiciona_aresta(a2)
paraiba.adiciona_aresta(a3)
paraiba.adiciona_aresta(a4)
paraiba.adiciona_aresta(a5)
paraiba.adiciona_aresta(a6)
paraiba.adiciona_aresta(a7)
paraiba.adiciona_aresta(a8)
paraiba.adiciona_aresta(a9)

print(paraiba)



