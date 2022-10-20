from re import A
import numpy as np

def transformationint(a):
    return int(a)
def promedios(list):
    return sum(list)/len(list)
def imprimir(data,prom):
    o = []
    o.append(data[0])
    for i in range(len(data)-1):
        o.append(data[i+1].append(prom[i]))
    return o

r = np.genfromtxt("calificaciones_v1.csv", delimiter = ',',dtype=str)

r = r.transpose()

titles = list(r[0][:9])

titles.append("Promedios")

newList = []
numbers = []
newList.append(titles)
for i in range(int(len(r[1])/9)):

    a = list(r[1][i*9:i*9+9])
    n = list(a[3:8])
    newList.append(a)

    numbers.append(list(map(transformationint,n)))

prom = list(map(promedios,numbers))
a = imprimir(newList,prom)
print(a)
 #3-8