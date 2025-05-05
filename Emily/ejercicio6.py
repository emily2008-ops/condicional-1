nombre1=input("ingrese el nombrre del primer hermano: ")
edad1=int(input("ingresela edad del primer hermano: "))

nombre2=input("ingrese el nombre del segundo hermano: ")
edad2=int(input("ingrese el nombre del segundo hermano: "))

if edad1 > edad2:
    print("el hermano mayor es: ", nombre1)
elif edad2 > edad1:
    print("el hermano mayor es: ", nombre2) 
    print("ambos tienen la misma edad. ")