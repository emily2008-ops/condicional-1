placa1 = input("Ingrese la placa del primer bus: ")
pasajeros1 = int(input("Ingrese el número de pasajeros transportados por el bus 1: "))
valor_pasaje1 = float(input("Ingrese el valor del pasaje del bus 1: "))
dinero1 = pasajeros1 * valor_pasaje1

placa2 = input("Ingrese la placa del segundo bus: ")
pasajeros2 = int(input("Ingrese el número de pasajeros transportados por el bus 2: "))
valor_pasaje2 = float(input("Ingrese el valor del pasaje del bus 2: "))
dinero2 = pasajeros2 * valor_pasaje2

if dinero1 > dinero2:
    print("El bus que más dinero recogió fue el de placa )", placa1, dinero1)
elif dinero2 > dinero1:
    print("El bus que más dinero recogió fue el de placa )",placa2, dinero2)
else:
    print("Ambos buses recogieron el mismo dinero: ",dinero1)