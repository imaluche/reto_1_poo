def oper(a,b,o): #definimos la funcion con 3 entradas. Los dos operandos y el operador
    if o == '+':
        return a + b
    if o== '-':
        return a - b
    if o == '*':
        return a * b
    if o == '/':
        return a / b
    # definimos una funcion que reconozca los simbolos de cada operador para hacer la operacion deseada
if __name__=="__main__":
    num1=float(input("primer operando: "))
    num2=float(input("segundo operando: "))
    opera=(input("operador(+,-,* o /): "))
    # creamos variables que permitan ser ingresadas por teclado por el usuario
    print("el resultado es "+ str(oper(num1,num2,opera)))

