# Calculadora sencilla con validaciones y funciones
# Autor: Frank Hernández
# Polaris – Fase 0B, Hora 1

# Mensaje inicial y menú de operaciones
print("Bienvenido, seleccione la operación que desee realizar")
operaciones = [
    "1. Suma",
    "2. Resta",
    "3. Multiplicación",
    "4. División",
    "5. Salir"
]
error = "Ingrese un número válido"

# Función que pide dos números y maneja errores con try/except
def pedir_numeros():
    try:
        n1 = float(input("Ingrese la primera cifra: "))
        n2 = float(input("Ingrese la segunda cifra: "))
        return n1, n2  # Devuelve los dos números si todo está bien
    except ValueError: # Aquí le decimos a python el tipo de error
        print("Error: solo se permiten números.")
        return None, None  # Si hay error, devuelve valores vacíos para evitar fallos

# Bucle principal que muestra el menú y procesa la opción del usuario
while True:
    print("\nOperaciones disponibles:")
    for op in operaciones:    # iteramos en el la lista e imprimimos cada valor
        print(op)

    ops = input("Seleccione una opción (1-5): ")

    # Operación 1: Suma
    if ops == "1":
        num1, num2 = pedir_numeros()
        if num1 is not None:
            print("Resultado:", num1 + num2)

    # Operación 2: Resta
    elif ops == "2":
        num1, num2 = pedir_numeros()
        if num1 is not None:
            print("Resultado:", num1 - num2)

    # Operación 3: Multiplicación
    elif ops == "3":
        num1, num2 = pedir_numeros()
        if num1 is not None:
            print("Resultado:", num1 * num2)

    # Operación 4: División con validación de división por cero
    elif ops == "4":
        num1, num2 = pedir_numeros()
        if num1 is not None:
            if num2 == 0:
                print("No se puede dividir por cero.")
                continue  # Vuelve al menú sin mostrar resultado
            print("Resultado:", num1 / num2)

    # Opción 5: Salir del programa
    elif ops == "5":
        print("Gracias por usar la calculadora.")
        break  # Termina el bucle y el programa

    # Cualquier otra opción no válida
    else:
        print(error)
