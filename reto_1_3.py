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