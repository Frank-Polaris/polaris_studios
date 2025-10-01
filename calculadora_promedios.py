# Este programa calcula el promedio de una lista de números ingresados por el usuario (versión while)
print("\nBienvenido, este programa calcula el promedio de una lista de números ingresados")
while True:
    entrada_usuario = input("\n¿Cuántas entradas desea promediar? (o escriba 'exit' para salir): ")
    
    if entrada_usuario.lower() == "exit":
        print("Gracias por usar la calculadora.")
        break  # Salir del bucle correctamente

    try:
        num = int(entrada_usuario)
    except ValueError:
        print("Error: solo se aceptan números enteros.")
        continue

    entrada = []

    for i in range(num):
        try:
            cifra = float(input(f"Ingrese la cifra #{i+1}: "))
            entrada.append(cifra)
        except ValueError:
            print("Error: ingrese un número válido.")
            continue

    promedio = sum(entrada) / len(entrada)
    print("El promedio es:", promedio)


      
    