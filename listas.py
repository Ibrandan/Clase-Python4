from this import d
from re import A

dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]
numeros = [7, 14, 21]
listaVacia = []
listaCompuesta = ["hola", 2.0, 5, [10, 20, 30, 40, 50]]

# dias al ser una lista se puede modificar
dias[1] = "tuesday"
print(dias)  # Imprime todos los elementos de la lista
print(dias[-1])  # Imprime el ultimo elemento de la lista

print(numeros)
print(numeros[1])
# ^ Equivalente a:
print(numeros[3-2])

print(listaCompuesta)
# En este caso imprime el elemento en la posicion 3, el ultimo
print(listaCompuesta[3])
# Se puede recorrer tambien la lista interior que esta dentro de la lista compuesta indicando el indice de forma encadenada, el 3 representa el indice 3 en la lista compuesta y el 1 representa el indice 1 en la lista interior
print(listaCompuesta[3][1])

# Se genera una lista a partir del range con el constructor list / range(2,6) genera una lista del 2 al 5 sin incluir al 6
listaNumeros1 = list(range(2, 6))
# al no declarar el inicio, se toma al 0 como inicio
listaNumeros2 = list(range(10))
listaNumeros3 = list(range(1, 10, 2))
print(listaNumeros1)
print(listaNumeros2)
print(listaNumeros3)  # imprime del 1 al 9 saltando un numero


# recorrer listas
# while
i = 0                       # ---> iniciamos una variable para utilizar como contador
while i < len(dias):           # similar a array.length en js
    print(dias[i])
    i += 1

print("------------")

for dia in dias:
    print(dia)

print("------------")

for p in range(len(dias)):
    print(dias[p])

# ^ equivalente a:

for p in range(0, len(dias)):
    print(dias[p])

if "tuesday" in dias:           # ----> Evalua si un elemento, en este caso "tuesday", esta dentro de la lista
    print("lo encontre")


# Las listas tienen operaciones
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b  # Se concatenan las listas
print(c)  # c tiene los elementos de ambas listas dentro de una sola

print(a * 3)  # imprime tres veces los elementos de a en una lista

# Slicing

lista = ["a", "b", "c", "d", "e", "f"]
#            0    1     2    3     4    5

# imprime los elementos de las posiciones 1 y 2 de la lista, se excluye al 3
print(lista[1:3])
# imprime los elementos de las posiciones 0 hasta la 3 de la lista, se excluye al 4
print(lista[:4])
print(lista[3:])  # imprime desde el 3er elemento hasta el el ultimo
print(lista[:])  # imprime la lista completa

# la funcion del elimina el elemento que se indica dentro del parametro
del(lista[1])
print(lista)


# Clonar lista

listaClonada = [1, 3, 5]
# Agrega desde la posicion 3 la lista ya creada anteriormente
listaClonada[3:] = lista[:]
print(listaClonada)

# Pilas
# LIFO: Last in first out / El ultimo en entrar, es el primero en salir
listado = ["a", "b", "c", "d", "e", "f"]

# la funcion append agrega al final de la lista el elemento ingresado por parametro
listado.append("g")
listado.append("h")
listado.append("i")
print(listado)

# Para remover un elemento, como el ultimo en entrar es el primero en salir, debemos remover los elementos del final

listado.pop()  # Esta funcion elimina el ultimo elemento de la lista
print(listado)

# Insertar un valor en una posicion determinada lo hacemos con la funcion insert. En los parametros,  primero se indica el indice o lugar donde se quiere insertar y luego el objeto
lista.insert(2, "ch")
print(lista)

# Para remover un elemento de una lista lo hacemos con la funcion remove que recibe como parametro el elemento que se quiere remover. Si hay mas de un elemento remueve el primero
lista.remove("ch")
print(lista)


# El metodo index nos permite averiguar cual es el indice del elemento que pasamos por parametro
print(lista.index("d"))


# Sorted: La funcion sorted nos permite ordenar numeros de una lista de forma ascendente
numerosDesordenados = [8, 1, 6, 9]
print(sorted(numerosDesordenados))

# Named parameter
# Imprime los numeros en orden descendente
print(sorted(numerosDesordenados, reverse=True))


# definimos un valor por defecto para los parametros, tomara esos valores si a la funcion la llaman si parametro
def imprimirLista(reverse=False, list=[]):
    if reverse:
        for i in reversed(range(len(list))):  # Ordena los numeros en forma descendente
            print(list[i])  # Imprime cada elemento de la lista
    else:
        for elem in list:   # Si reverse es falso los imprime en el orden ascendente
            print(elem)


imprimirLista(list=[1, 5, 6, 7])
print("-------------")
# Si se ingresa el parametro con su nombre se puede invertir el orden
imprimirLista(list=[1, 5, 6, 7], reverse=True)
# Acá no se puede invertir el orden de los parametros
imprimirLista(True, [1, 19, 20])
