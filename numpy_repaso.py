import numpy as np

print(np.__version__)

lista = [1,2,3,4,3]



array = np.array(lista)

print(array.ndim) #Numero de dimensiones
print(array.shape)
print(array.size)
print(array.dtype)
print(array.itemsize)
print(array.data)
print(type(array))
print(array.max())
print(array.min())


lista1=[1,2,3,4,3]
lista2=[4,5,6]

array = np.array([lista1,lista2], dtype=object)

print("-----------------")

print(array.ndim)
print(array.shape)
print(array.size)
print(array.dtype)
print(array.itemsize)
print(array.data)
print(type(array))
print(array.max())
print(array.min())

print("---------------")
lista1=[1,2,3,4,1]
lista2=[4,5,6]
lista3=[6,7,8,9]
array = np.array([lista1,lista2,lista3], dtype=object)
print(array.ndim)
print(array.shape)
print("-------------------")
array=np.arange(5)
print(array)
array = np.zeros((3,4))
print(array)
array = np.ones((4,3))
print(array)
array = np.linspace(1,9,10)
print(array)

print("-----------------")
array = np.array([1,3,3])

print(array.argmax()) #index del numero mayor
print(array.argmin()) #index
print(array.max()) #value
print(array.min()) #value

#help(array)
array2 = array.copy()
array = array.astype(dtype = float)
array2.fill(0)
print(array)
print(array2)

array.dump("datos.pk") #pickle

x = np.load("datos.pk", allow_pickle = True)
print(x)

array = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype = np.int64)
print(array)

print(array.flatten())
print(array.item(4))
array = np.array([0,1,0,3,4,0],dtype = np.int64)
print(array.nonzero())#indices donde no hay ceros

array = np.array([1,2,3])
print(array.prod())
array2 = array.copy()
print(array.prod(initial = 13))
array.put(1,4)
print(array)
array = np.array([1,2,3])
print(array.repeat(repeats=3))
array = array.repeat(repeats=3)
print(array.reshape(3,3))#(rows,cols)
print(array)
array = array.reshape(3,3)
print(array)
array = array.reshape(1,9)
print(array)
array = np.array([[1,2],[3,4]],dtype = np.int64)
print("---------------------------------------------")
print(array)

print(np.resize(array,(1,3)))

array = np.array([[1,2,3],[4,1,2],[3,4,1],[2,3,4]], dtype=np.int64)
print(array)
array.sort(axis=1,kind='quicksort')
print(array)
# 0 - cols
# 1 - rows
array.sort(axis=0,kind='quicksort')
print(array)

print("----------------")

array = np.array([[0,1],[2,3]], dtype = np.int64)
print(array)
print(array.swapaxes(1,0))
print("------------------------------")
array = np.array([1,2,3,4,5], dtype=np.int64)
print(array.take((2,4)))
print("-----------------------------------------------aa")

a = np.array(["Unos","Dos Dos","Tres"])
print(np.char.center(a,10,"-"))
print(np.char.count(a,"os")) #Contar cuantas veces aparece os en cada uno de los elementos
print(np.char.find(a,"os")) #busca de izquierda a derecha
print(np.char.rfind(a,"os")) #busca de derecha a izquierda
print(np.char.index(a,"s")) #si no encuentra el error en  algun valor manda error
print(np.char.rindex(a,"s"))
print("----------------------")

a = np.array(["Hola","3","Hola3","\t"])
print(np.char.isalnum(a))
print(np.char.isdecimal(a))
print(np.char.isalpha(a))
print(np.char.isnumeric(a))
print(np.char.isspace(a))
print(np.char.istitle(a))

print("------------------------------------------")
a = np.random.rand(2,3)
print(a)#Row Col
print(a[0,0:1])
print(a[:,0])
print(a[1,0:1])
print(a[0,:])
print("------------------------------------------")

