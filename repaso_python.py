# Cadenas
def prueba():
    for i in range(4):
        for j in range(i+1):
            print("*",end="")
        print("")

    cadena = "Hola como estan"

    for i in range(len(cadena)):
        print(cadena[len(cadena)-1-i],end="")
    print("")

    print(cadena.__len__())

    st= "A"

    print(st.__eq__("A"))

    print(st.__add__("A"))

    query ="delete * from contactos where id = 1;"

    reserved_words = ["select","create","update","delete", "primary key", "not", "null", "from","where"]

    query = query.split(" ")

    new =""

    for i in range(len(query)):
    
        if query[i] in reserved_words:
            new += query[i].upper()+" "
            print(query[i].upper()+" ",end="")
        else:
            new += query[i]+" "
            print(query[i]+" ",end="")

    print()

    print(new)

    query = "select * from clientes where id = 1;"

    for i in reserved_words:
        query= query.replace(i,i.upper())

    print(query)

def formatesQuerySQL(query:str)->str:
    reserved_words = ["select","create","update","delete", "primary key", "not", "null", "from","where"]

    for i in reserved_words:
        query = query.replace(i,i.upper())
    return query


formatesQuerySQL("select * from consultas where id = ;")

consultas = ["select * from consultas where id = 1;","select * from clases;"]


new = list(map(formatesQuerySQL,consultas))

print(new)
