def sprint(value:str):
    value = value.split(",")
    return value

def FormatFile():
    data = []
    with open("archivo.csv","r") as file:
        for i in file:
            data.append(i.replace("\n",""))
    data = list(map(sprint,data))
    return data

def CountAllLines(data:list):
    return len(data)

def dates(data:list):
    return data[0]

def removeDates(data:list):
    del data[0]
    return data

def convertallValuesinNumber(data:list):
    newdata= []
    for i in data:
        newdata.append(float(i))
    return newdata

def maxValue(data:list):
    maximo = max(data)
    return maximo

def minValue(data:list):
    minimo = min(data)
    return minimo

def totalValues(data:list):
    return len(data)

def sumValues(data:list):
    result = sum(data)
    return(result)

def prom(data:list):
    data = sum(data)/len(data)
    return data

def printFormates(dates:list,values:list,maximos:list,minimos:list,totales:list,promedios:list):
    for i in range(len(dates)):
        print(f"{dates[i]} - Valores({values[i]}), Maximo({maximos[i]}), Minimo({minimos[i]}), Total({totales[i]}), Promedio ({promedios[i]})")


data = FormatFile()
dates= list(map(dates,data))
data = list(map(removeDates,data))
data = list(map(convertallValuesinNumber,data))
values = list(map(totalValues,data))
maximos = list(map(maxValue,data))
minimos = list(map(minValue,data))
totales = list(map(sumValues,data))
promedios = list(map(prom, data))
printFormates(dates,values,maximos,minimos,totales,promedios)
numberLines = CountAllLines(data)
print(f"Número de filas: {numberLines}")