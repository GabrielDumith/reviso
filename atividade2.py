numero=int(input("digite o numero: "))
resposta = "sim"
while resposta== "sim":
    if numero > 0 and numero %2 ==0:
            print(f"{numero} par e positivo")
    elif numero > 0 and numero%2!=0:
            print(f"{numero}impa e positivo")
    elif numero > 0 and numero % 2 != 0:
            print(f"{numero}impa negativo")
    elif numero > 0 and numero % 2 == 0:
            print(f"{numero}par negativo")
    resposta=input("quer fazer novamente")