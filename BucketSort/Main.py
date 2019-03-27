import random
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import itertools as it
mpl.use('Agg')

def geraLista(tam):
    lista = []
    for i in range(tam):
        lista.append(i)
    random.shuffle(lista)
    return lista

def geraListaCre(tam):
    lista = []
    for i in range(tam):
        lista.append(i)
    return lista

def geraListaDec(tam):
    lista = []
    n = tam
    for i in range(tam):
        lista.append(n)
        n -=1
    return lista

def bucket_sort(alist):
    largest = max(alist)
    length = len(alist)
    size = largest/length
 
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(alist[i]/size)
        if j != length:
            buckets[j].append(alist[i])
        else:
            buckets[length - 1].append(alist[i])
 
    for i in range(length):
        insertion_sort(buckets[i])
 
    resposta = []
    for i in range(length):
        resposta = resposta + buckets[i]
 
    return resposta
 
def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp

def desenhaGrafico(x, piorcaso, melhorcaso, aleatorio, name, xl = "Entradas", yl = "Tempo (s)"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, piorcaso, label = "Pior Caso")
    ax.plot(x, melhorcaso, label="Melhor Caso")
    ax.plot(x, aleatorio, label="Aleatório")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(name)

x = [10000, 20000, 30000, 40000, 50000]

PiorCaso = []
MelhorCaso = []
CasoAle = []

for i in x:
    lista = geraListaDec(i)
    PiorCaso.append(timeit.timeit('bucket_sort({})'.format(lista),setup="from __main__ import bucket_sort",number=1))
    
    lista = geraLista(i)
    CasoAle.append(timeit.timeit('bucket_sort({})'.format(lista),setup="from __main__ import bucket_sort",number=1))
    
    lista = geraListaCre(i)
    MelhorCaso.append(timeit.timeit('bucket_sort({})'.format(lista),setup="from __main__ import bucket_sort",number=1))

desenhaGrafico(x, PiorCaso, MelhorCaso, CasoAle, "graph_time.png")

lis = [1, 2, 3, 4, 5, 6]
permut = list(it.permutations(lis,6))
tempo = []
listaok = []

for i in permut:
  listaok.append(list(i))

for i in range(len(listaok)):
    tempo.append(timeit.timeit('bucket_sort({})'.format(listaok[i]),setup="from __main__ import bucket_sort",number=1))

maior = tempo.index(max(tempo))
menor = tempo.index(min(tempo))

print('Tempo maior:',max(tempo))
print(permut[maior])
print("\n")
print('Tempo menor:',min(tempo))
print(permut[menor])
