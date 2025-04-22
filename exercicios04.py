altura=float(input("digite sua altura"))
peso=float(input("digite seu peso "))
imc=peso/altura*altura

if imc<18.6:
    print("abaixo do peso")
elif imc >=18.6 and imc< 24.9:
    print("")