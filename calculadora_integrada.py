# calculadora_integral.py — Polaris Fase 0C, Hora 4

# === MENÚ PRINCIPAL ===
def menu_principal():
    while True:
        try:
            menu = int(input("""\nMenú Principal:
1. Operaciones Básicas
2. Calculadora de Promedios
3. Validador de Edades
4. Salir del programa
Seleccione una opción: """))
        except ValueError:
            print("Error: ingrese un número del 1 al 4.")
            continue

        if menu == 4:
            print("\nGracias por usar la calculadora integrada creada por Frank y Polaris :) ")
            break
        elif menu == 1:
            operaciones_basicas()
        elif menu == 2:
            promedios()
        elif menu == 3:
            validar_edades()
        else:
            print("Opción no válida.")

# === OPERACIONES BÁSICAS ===
def operaciones_basicas():
    operaciones = [
        "1. Suma",
        "2. Resta",
        "3. Multiplicación",
        "4. División",
        "5. Salir al menú principal"
    ]

    def pedir_numeros():
        try:
            n1 = float(input("Ingrese la primera cifra: "))
            n2 = float(input("Ingrese la segunda cifra: "))
            return n1, n2
        except ValueError:
            print("Error: solo se permiten números.")
            return None, None

    while True:
        print("\nOperaciones disponibles:")
        for op in operaciones:
            print(op)

        ops = input("Seleccione una opción (1-5): ")

        if ops == "1":
            num1, num2 = pedir_numeros()
            if num1 is not None:
                print("Resultado:", num1 + num2)
        elif ops == "2":
            num1, num2 = pedir_numeros()
            if num1 is not None:
                print("Resultado:", num1 - num2)
        elif ops == "3":
            num1, num2 = pedir_numeros()
            if num1 is not None:
                print("Resultado:", num1 * num2)
        elif ops == "4":
            num1, num2 = pedir_numeros()
            if num1 is not None:
                if num2 == 0:
                    print("No se puede dividir por cero.")
                    continue
                print("Resultado:", num1 / num2)
        elif ops == "5":
            print("Volviendo al menú principal...")
            break
        else:
            print("Ingrese un número válido")

# === CALCULADORA DE PROMEDIOS ===
def promedios():
    print("\nCalculadora de Promedios")
    while True:
        entrada_usuario = input("\n¿Cuántas entradas desea promediar? (o escriba 'exit' para salir al menú principal): ")

        if entrada_usuario.lower() == "exit":
            print("Volviendo al menú principal...")
            break

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

# === VALIDADOR DE EDADES ===
def validar_edades():
    print("\nValidador de Edad")

    def verificador():
        entrada = input("Ingrese su edad (o escriba 'salir'): ")
        if entrada.lower() == "salir":
            return "salir"
        try:
            edad = int(entrada)
            return edad
        except ValueError:
            print("Error: solo se permiten números enteros.")
            return None

    while True:
        edad = verificador()

        if edad == "salir":
            print("Volviendo al menú principal...")
            break

        if edad is not None:
            if edad < 0 or edad > 120:
                print("Edad no válida.")
                continue

            if edad <= 3:
                print("Es un bebé.")
            elif edad <= 12:
                print("Es un niño.")
            elif edad < 18:
                print("Es adolescente.")
            elif edad < 25:
                print("Es adulto joven.")
            elif edad < 59:
                print("Es adulto.")
            else:
                print("Es adulto mayor.")

# === EJECUCIÓN ===
menu_principal()
