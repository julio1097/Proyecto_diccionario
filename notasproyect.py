estudiantes= []
notas= []
opc= -1
while opc !=4:
	print("1. Estudiante")
	print("2. Ingresar")
	print("3. Reporte")
	print("4. Salir")
	continuar = "si"
	opc= int(input("Ingrese opcion a realizar: "))
	while opc >=5 or opc <=0:
		print ("Opcion invalida :v")
		opc= int(input("Ingrese opcion a realizar (1- 4): "))
	if opc== 1:
		while continuar== "si":
			nombre= str(input("Ingrese el nombre del estudiante: "))
			estudiantes.append(nombre)
			continuar= str(input("¿Desea continuar? (si/no): "))		
		print(estudiantes)
	if opc== 2:
		while continuar== "si":
			nombre= str(input("Ingrese el nombre del alumno al que deseea agregar nota: "))
			nombre in estudiantes
			nota= str(input("Ingrese su nota: "))
			notas.append(nota)
			continuar= str(input("¿Desea continuar? (si/no): "))
		print(notas)
	if opc== 3:
		print(estudiantes)
		print(notas)
		promedio= sum(notas) / len(notas)
		print(promedio)
	if opc== 4:
		exit ()