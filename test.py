import math
import time

#Ejercicio 1: Definir las siguientes funciones y procedimientos:

'''
Ejercicio 1.1
problema imprimir_hola_mundo () {
requiere: { T rue }
asegura: { imprime "¡Hola mundo!"por consola}
}
'''

def imprimir_hola_mundo() -> str:
    print("Hola mundo")

'''
Ejercicio 1.2
imprimir_un_verso(): que imprima un verso de una canción que vos elijas, respetando los saltos de línea mediante
el caracter \n
'''

def imprimir_un_verso() -> str:
    print("We'll meet again\nDon't know where\nDon't know when\nBut I know we'll meet again some sunny day")

'''
Ejercicio 1.3
raizDe2(): que devuelva la raíz cuadrada de 2 con 4 decimales. Ver función round
'''

def raizDe2() -> float:
    res:float = round(math.sqrt(2), 4)
    return res
x:float = raizDe2()

'''
Ejercicio 1.5
perimetro: que devuelva el perímetro de la circunferencia de radio 1. Utilizar la biblioteca math mediante el comando
import math y la constante math.pi
problema perimetro () : R {
requiere: { T rue }
asegura: {res = 2 × π }
}
'''

def perimetro() -> float:
    res:float = 2*math.pi
    return res
y:float = perimetro()

#Ejercicio 2. Definir las siguientes funciones y procedimientos con parámetros:

'''
Ejercicio 2.5
problema es_multiplo_de (in n: Z, in m:Z) : Bool {
requiere: {m /= 0}
asegura: {(res = true) ↔ (existe un k ∈ Z tal que n = m × k)}
}
'''

def es_multiplo_de(n: int, m: int) -> bool:
    res:bool = (n % m) == 0
    return res
z:bool = es_multiplo_de(6,3)

#Ejercicio 3. Resuelva los siguientes ejercicios utilizando los operadores lógicos and, or, not.
#Resolverlos sin utilizar alternativa condicional (if).

'''
Ejercicio 3.3
problema es_nombre_largo (in nombre: String) : Bool {
requiere: { True }
asegura: {(res = true) ↔ (3 ≤ |nombre| ≤ 8)}
}
'''

def es_nombre_largo(nombre: str) -> bool:
    res:bool = (3 <= len(nombre)) and (len(nombre) <= 8)
    return res

a:bool = es_nombre_largo("Lucas")

#Implementar los siguientes problemas de alternativa condicional (if/else).
#Los enunciados pueden no ser del todo claros, especificar los problemas en nuestro
#lenguaje de especificación y programar en base a tu propuesta de especificación.

'''
Ejercicio 5.1
devolver_el_doble_si_es_par(numero); que devuelve el doble del número en caso de ser par y el mismo número en
caso contrario.
'''

def devolver_el_doble_si_es_par(n: int) -> int:
    res:int
    if (n % 2) == 0:
        res = n*2
    else:
        res = n
    return res
b:int = devolver_el_doble_si_es_par(2)

#Ejercicio 6. Implementar las siguientes funciones usando repetición condicional while:

'''
Ejercicio 6.2*
Escribir una función que imprima los números pares entre el 10 y el 40.
'''

def imprimir_pares_10_40() -> int:
    i:int = 10
    while (i <= 40):
        print(i)
        i = i + 2

def otro_imprimir_pares_10_40() -> int:
    i:int
    for i in range [10:40,2]:
        print(i)