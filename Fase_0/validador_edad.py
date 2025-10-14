# Este es un programa validador de edad
# Polaris — Fase 0B, Hora 2 – Versión extendida

print("\nBienvenido, este es un validador de edad")

# Función para pedir y validar la edad
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

# Bucle principal
while True:
    edad = verificador()
    
    if edad == "salir":
        print("Gracias por usar el verificador de edad.")
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


        
    
       
