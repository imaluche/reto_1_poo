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
   
        
    