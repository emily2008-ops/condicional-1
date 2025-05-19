edad= int(input("inegrese la edad: "))

if edad < 10:
    print("Es un niño.")
elif 10 <= edad < 15:
    print("En un preadolecente. ")
elif 15 <= edad < 18:
    print("Es un adolecente. ")
elif 18 <= edad <=50:
    print("Es un adulto. ")
else:
    print("Es un adulto mayor")
