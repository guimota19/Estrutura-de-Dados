print("= = = C A L C U L A D O R A = = =")
n1 = input("Numero 1: ")
n2 = input("Numero 2: ")
op = input("Operador: ")

if(op=="+"):
    res = int(n1) + int(n2)
    print("Resultado ", res)

elif(op=="-"):
    res = int(n1) - int(n2)
    print("Resultado ", res)

elif(op=="*"):
    res = int(n1) * int(n2)
    print("Resultado ", res)

elif(op=="/"):
    res = int(n1) / int(n2)
    
    print("Resultado ", res)

else:
    print("Operação inválida.")
    