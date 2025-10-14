# ================================================================
# 🚢 PROYECTO: Limpieza y exportación de datos de buques
# Autor: Frank Hernández
# Fase 1 – Bloque R7
# Descripción:
#   Lee un archivo de texto con datos de barcos,
#   limpia los registros incompletos o duplicados,
#   ordena por año y exporta un archivo CSV limpio y ordenado.
# ================================================================

import csv  # Módulo estándar para manejar archivos CSV en Python

# Lista donde se guardarán los registros válidos
barcos_limpios = []

# Separador visual en consola
print("\n" + "*" * 80 + "\n")

# ------------------------------------------------
# 1️⃣ LECTURA DEL ARCHIVO ORIGINAL
# ------------------------------------------------
# Abrimos el archivo .txt (simula un CSV con posibles errores)
# encoding="utf-8" garantiza compatibilidad con caracteres latinos.
with open("barcos_sucios.txt", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)      # Crea el lector CSV (separa por comas)
    heading = next(lector)            # Salta la primera línea (encabezados)

    # Recorremos cada línea del archivo
    for line in lector:
        if len(line) != 4:
            continue  # Si no hay 4 columnas, se descarta la fila

        # Eliminamos espacios extra y capitalizamos cada campo
        nombre, pais, año, tonelaje = [v.strip().capitalize() for v in line]

        # Validamos que no haya campos vacíos
        if not nombre or not pais or not año or not tonelaje:
            continue

        # Intentamos convertir año y tonelaje a número entero
        try:
            año = int(año)
            tonelaje = int(tonelaje)
        except ValueError:
            continue  # Si no se puede convertir, descartamos la fila

        # Evitamos duplicados (por nombre + año)
        if not any(b["nombre"] == nombre and b["año"] == año for b in barcos_limpios):
            barcos_limpios.append({
                "nombre": nombre,
                "pais": pais,
                "año": año,
                "tonelaje": tonelaje
            })

# ------------------------------------------------
# 2️⃣ ORDENAMIENTO DE LOS REGISTROS
# ------------------------------------------------
# Ordenamos por año (ascendente). Si prefieres del más nuevo al más antiguo:
# barcos_limpios.sort(key=lambda b: b["año"], reverse=True)
barcos_limpios.sort(key=lambda b: b["año"])

# ------------------------------------------------
# 3️⃣ IMPRESIÓN EN CONSOLA
# ------------------------------------------------
# Mostramos los resultados limpios y ordenados
for b in barcos_limpios:
    print(f"Buque: {b['nombre']}, Bandera: {b['pais']}, Año: {b['año']} -- {b['tonelaje']} UAB")

# Mostramos un resumen final
print("\nTotal de barcos limpios:", len(barcos_limpios))
print("\n" + "*" * 80 + "\n")

# ------------------------------------------------
# 4️⃣ EXPORTACIÓN A CSV FINAL
# ------------------------------------------------
# Creamos un nuevo archivo limpio y ordenado para futuras fases (SQLite, BI, etc.)
with open("barcos_ordenados.csv", "w", encoding="utf-8", newline="") as salida:
    escritor = csv.writer(salida)  # Inicializamos el escritor CSV

    # Escribimos la fila de encabezados (nombres de columnas)
    escritor.writerow(["nombre", "pais", "año", "tonelaje"])

    # Escribimos cada barco como una fila del CSV
    for b in barcos_limpios:
        escritor.writerow([b["nombre"], b["pais"], b["año"], b["tonelaje"]])

# Mensaje final de confirmación
print("✅ Archivo 'barcos_ordenados.csv' generado correctamente.")
print("\n" + "*" * 80 + "\n")

