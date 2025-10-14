# catalogo_juegos.py — Polaris Fase 0C, Hora 5

# Lista para guardar los juegos
catalogo = []

# Menú principal
def menu():
    while True:
        print("""\n📀 Catálogo de Juegos
1. Agregar juego
2. Ver todos los juegos
3. Buscar por título
4. Ver estadísticas
5. Salir
""")
        opcion = input("Selecciona una opción (1-5): ")
        if opcion == "1":
            agregar_juego()
        elif opcion == "2":
            mostrar_catalogo()
        elif opcion == "3":
            buscar_juego()
        elif opcion == "4":
            estadisticas()
        elif opcion == "5":
            print("Saliendo del catálogo. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

# Función 1: Agregar juego
def agregar_juego():
    titulo = input("Título del juego: ")
    genero = input("Género: ")
    try:
        año = int(input("Año de lanzamiento: "))
    except ValueError:
        print("Año inválido.")
        return

    juego = {"titulo": titulo, "genero": genero, "año": año}
    catalogo.append(juego)
    print("Juego agregado con éxito.")

# Función 2: Mostrar todos los juegos
def mostrar_catalogo():
    if not catalogo:
        print("No hay juegos en el catálogo.")
        return
    for i, juego in enumerate(catalogo, 1):
        print(f"{i}. {juego['titulo']} ({juego['genero']}, {juego['año']})")

# Función 3: Buscar por título
def buscar_juego():
    consulta = input("Título a buscar: ").lower()
    encontrados = [j for j in catalogo if consulta in j["titulo"].lower()]
    if encontrados:
        for j in encontrados:
            print(f"🎮 {j['titulo']} ({j['genero']}, {j['año']})")
    else:
        print("No se encontraron juegos con ese título.")

# Función 4: Ver estadísticas
def estadisticas():
    if not catalogo:
        print("Catálogo vacío.")
        return
    total = len(catalogo)
    generos = set(j["genero"] for j in catalogo)
    print(f"Total de juegos: {total}")
    print(f"Géneros únicos: {', '.join(generos)}")

# Ejecutar menú
menu()
