nombre1 = input("Ingrese el nombre del primer trabajador: ")
salario_bruto1 = float(input("Ingrese el salario bruto de " + nombre1 + ": "))
deducciones1 = float(input("Ingrese las deducciones de " + nombre1 + ": "))
bonificaciones1 = float(input("Ingrese las bonificaciones de " + nombre1 + ": "))
salario_neto1 = salario_bruto1 - deducciones1 + bonificaciones1

nombre2 = input("\nIngrese el nombre del segundo trabajador: ")
salario_bruto2 = float(input("Ingrese el salario bruto de " + nombre2 + ": "))
deducciones2 = float(input("Ingrese las deducciones de " + nombre2 + ": "))
bonificaciones2 = float(input("Ingrese las bonificaciones de " + nombre2 + ": "))
salario_neto2 = salario_bruto2 - deducciones2 + bonificaciones2

if salario_neto1 > salario_neto2:
    print("El trabajador con mayor salario neto es: ", nombre1, salario_neto1)
elif salario_neto2 > salario_neto1:
    print("El trabajador con mayor salario neto es: )",nombre1, salario_neto1)
else:
    print("Ambos trabajadores tienen el mismo salario neto: ",salario_neto1)