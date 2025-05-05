Edad = int(input("Ingese la edad"))
Licencia = input("Ingrese licencia si o no")
if Edad>18 and Licencia=="si":
    print("Puede conducir")
elif Edad<18 and Licencia=="no":
    print("No puede conducir")
else:
    print("Error")        