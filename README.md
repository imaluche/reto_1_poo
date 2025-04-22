# reto-1 programacion orientada a objetos

----------------------------------

### 1. Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación.

```python
def oper(a,b,o): #definimos la funcion con 3 entradas. Los dos operandos y el operador
    if o == '+':
        return a + b
    if o== '-':
        return a - b
    if o == '*':
        return a * b
    if o == '/':
        return a / b
    # la variable o permite que la funcion reconozca directamente los simbolos de cada operador para hacer la operacion deseada
if __name__=="__main__":
    num1=float(input("primer operando: "))
    num2=float(input("segundo operando: "))
    opera=(input("operador(+,-,* o /): "))
    # creamos variables que permitan ser ingresadas por teclado por el usuario
    print("el resultado es "+ str(oper(num1,num2,opera)))
```
#### explicacion:
- Definimos la funcion principal con 3 entradas que representen los valores a operar y el operador que se desea usar
- Dentro de la funcion se evaluara el tipo de operador, dependiendo de cual sea se realizara una u otra operacion y se retornara el resultado
- Dentro del codigo declaramos las 3 variables que se ingresaran a la funcion, estas variables se ingresaran por teclado y definiran los operandos y la operacion
- Aplicamos la funcion y la imprimimos de forma que sea comprensible
-----------------------------------
### 2. Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

```python
def detectorpalindromo(word:str): #la unica entrada sera la palabra que analizaremos
    long=(len(word)) #longitud de la palabra
    i=0
    s:list=[]
    e:list=[]
    for j in palabra:
        if long%2==0: #caso par
            if i<long/2:s.append(j) #primera mitad
            if i>=long/2: e.append(j) #segunda mitad
        else: #caso impar
            if i<(long-1)/2:s.append(j) #primera mitad 
            if i>(long-1)/2:e.append(j) #segunda mitad       
        i=i+1
    if sorted(s)==sorted(e): #comparamos ambas mitades ordenadas
        print("Es un palindromo")
    else:
        print("No es un palindromo")    
if __name__ == '__main__':
    palabra = input("Escribe una palabra: ")
    detectorpalindromo(palabra)
```
#### explicacion:
- Definimos una funcion en la que ingrese una cadena de caracteres (la palabra que se evaluara)
- Dentro de la funcion declaramos un valor inicializado en cero a modo de iterador y dos listas en las cuales se ingresaran las mitades de la palabra ingresada
- Por medio de bucle for se recorrera cada letra de la palabra
- Con un evaluador identificaremos si la palabra es par o impar, lo unico que cambia es el criterio para elegir la primera y segunda mitad
- En ambos casos se almacenaran las letras de la primera mitad de la palabra en una lista y las de la segunda mitad en otra
- Se compraran ambas listas ordenadas por medio de la funcion sorted con el fin de trabajar con elementos iguales en caso de ser palindromos
- Dependiendo del resultado de esta comparacion se llegara a una u otra conclusion la cual se imprimira en la consola
- Dentro del codigo declarararemos una variable ingresable por teclado para permitir al usuario ingresar la palabra a evaluar, hecho esto se aplicara la funcion en esta
-----------------------------------
### 3. Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.
```python
def generar_lista(n:int): 
    lista:list=[]
    for j in range(n):
        num=int(input("Escribe el numero (en caso de no ser entero se convertira a un entero): "))
        lista.append(num)
    print("Tu lista es: "+ str(lista))
    return lista
def primos(li:list):
    prime:list=[]
    for val in li: # recorremos la lista
        div:int=0
        comprobador:int=1
        while comprobador<=val:
            if val%comprobador==0:# comprobamos en que caso la division es entera
                div=div+1
            comprobador=comprobador+1
        if div==2: # un primo solo se puede dividir por 1 y por si mismo
            prime.append(val)
    print("los numeros primos de tu lista eran: "+ str(prime))
if __name__=="__main__":
    x = int(input("Cuantos numeros quieres ingresar a tu lista: "))
    listado:list = generar_lista(x)
    primos(listado)
```
#### explicacion:
- Definimos una funcion a la cual se ingresara una dato de tipo lista
- Dentro de la funcion por medio de un bucle for recorremos cada valor de la lista
- cada uno de estos valores pasara por un ciclo while dentro del cual se realizara la operacion de residuo con un numero desde 1 hasta el mismo valor
- Por medio de esta operacion podremos saber cuantas divisiones enteras tiene el valor evaluado
- En caso de que cuente solamente con 2 (caso de todo numero primo) esta se añadira a una nueva lista la cual solo contendra numeros primos
- Esta lista resultante se imprimira al final de la funcion de manera comprensible
- Dentro del codigo declararemos una variable para elegir la cantidad de valores de la lista y se generara una lista contenida en una variable a la cual se le aplicara la funcion
-----------------------------------

### 4. Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.
```python
from reto_1_3 import * #importamos las funciones del punto anterior
def mayor(l:list):
    l.sort(reverse=True) #ordenamos la lista ingresada de mayor a menor
    print("la mayor suma es: "+ str(l[0]+l[1])) #sumamos el primer y segundo elemento
if __name__=="__main__":
    n=int(input("Cuantos numeros quieres sumar? "))
    x=generar_lista(n)
    mayor(x)
```
### explicacion:
- Importamos la primera funcion del punto anterior para generar listas
- Definimos una funcion a la cual ingrese un dato del tipo lista
- Dentro de la funcion se usara el metodo .sort para organizar la lista, pero en este caso se definira la variable "reverse" como verdadera con el fin de que se organize de mayor a menor en orden lexicografico
- Hecho esto simplemente se suman los dos primeros valores de la lista, los cuales debido a la manera en la que se ordenaron siempre seran los dos mayores
- La funcion acabara imprimiendo el resultado de forma comprensible
- Dentro del codigo declaramos las variables que permitan al usuario decidir cuantos valores conformaran la lista y se aplicara la funcion en la lista generada 
-----------------------------------
### 5. Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres.
```python
def generar_listastr(n:int):
    lista:list = []
    for j in range(n):
        pal=input("Escribe la palabra (en caso de ser un numero el programa lo convertira en un string): ")
        lista.append(pal)
    print("Tu lista es: "+ str(lista))
    return lista  #generamos una lista compuesta unicamente por strings
def mismalet(li:list):
    repe:list = []
    for i in range (0,len(li)):
        for j in range (i+1,len(li)):
            if sorted(li[i])==sorted(li[j]):#comparamos cada palabra con las demas
                repe.append(li[i])
                repe.append(li[j])
    print("las palabras que comparten letras con otra palabra son: "+str(repe)) 
if __name__=="__main__":
    n=int(input("Cuantas palabras quieres agregar a la lista?: "))
    mismalet(generar_listastr(n))
```
### explicacion:
- Definimos una funcion que permita generar listas compuestas unicamente por strings (el unico cambio que realiza es no convertir el dato ingresado por teclado a flotante)
- Definimos una funcion a la cual ingresen unicamente listas
- dentro de la funcion recorreremos la lista de tal forma que con un segundo ciclo for se compare cada palabra con todas las demas que le siguen en la lista
- en caso de que al organizarse con la funcion sorted ambas palabran sean iguales estas se añadiran a una lista resultante
- La lista resultante se imprimira de forma que su informacion sea comprensible para el usuario
- Dentro del codigo se aplica la funcion en una lista generada por el usuario
