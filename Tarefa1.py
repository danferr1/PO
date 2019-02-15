from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt

def bubbleSort(lista):
  swaps = 0
  n = len(lista)
  for i in range(n):
      for j in range(n-i-1):
        swaps+=1
        if lista[j]> lista[j+1]:
          lista[j], lista[j+1] = lista[j+1], lista[j]
  return swaps


 
def geraLista(tam):
    lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista
 
mpl.use('Agg')
 
def desenhaGrafico(x, y,nome, xl = "Entradas", yl = "Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(nome)
  
x = [10000, 20000, 30000, 40000, 50000]
y = []

vetor = []
for i in range(len(x)):
    lista = geraLista(x[i])
    y.append(timeit.timeit("bubbleSort({})".format(lista),setup="from __main__ import bubbleSort",number=1))
    vetor.append(bubbleSort(lista))

desenhaGrafico(x,vetor,"Comparacoes.png")
desenhaGrafico(x, y, "Tempo.png")
