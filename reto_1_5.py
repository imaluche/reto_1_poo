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
