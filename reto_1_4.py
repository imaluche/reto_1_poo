from reto_1_3 import * #importamos las funciones del punto anterior
def mayor(l:list):
    l.sort(reverse=True) #ordenamos la lista ingresada de mayor a menor
    print("la mayor suma es: "+ str(l[0]+l[1])) #sumamos el primer y segundo elemento
if __name__=="__main__":
    n=int(input("Cuantos numeros quieres sumar? "))
    x=generar_lista(n)
    mayor(x)