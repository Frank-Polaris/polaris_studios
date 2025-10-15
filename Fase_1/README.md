# Fase 1 — Data Cleaning & CSV Export ⚓

**Objective:**  
Read, validate, clean, sort, and export structured CSV data using Python’s standard library (`csv`).

---

## 📘 Files

| File | Description |
|------|--------------|
| `barcos_sucios.txt` | Raw text file containing ships with duplicates and formatting issues. |
| `limpiar_y_exportar_barcos.py` | Main Python script for reading, cleaning, and exporting valid data. |
| `barcos_ordenados.csv` | Final cleaned and sorted dataset (UTF-8, comma-separated). |

---

## ⚙️ Script details

The script performs:
1. **Input validation** → checks each line for 4 valid fields.  
2. **Cleaning** → removes empty spaces, invalid rows, and duplicates.  
3. **Type conversion** → converts `año` and `tonelaje` to integers.  
4. **Sorting** → organizes the list of ships by construction year.  
5. **Export** → writes results to a new CSV with a header line.

---

## 🧩 Example output

Buque: Titanic, Bandera: Reino Unido, Año: 1912 -- 52310 UAB
Buque: Last Stop, Bandera: México, Año: 1998 -- 35000 UAB
...
Total de barcos limpios: 9
✅ Archivo 'barcos_ordenados.csv' generado correctamente.

---

## 🧠 Concepts learned
- File handling (`with open`, `csv.reader`, `csv.writer`)
- Data validation and type casting
- List comprehensions
- Duplicate control (`any()` logic)
- Sorting with `lambda`
- Clean exports for BI or database use

---

## 🚀 Next step
Move to **Fase 2 — SQLite integration**,  
where this clean CSV will be imported into a real database for SQL querying.
