monto = float (input("ingrese el monto total"))  
if monto >= 200:
  descuento = 0.20
elif monto >=100:
  descuento= 0.10
else: 
  descuento= 0
total=monto-(monto*descuento)
print ("monto con descuento aplicado: ", total)