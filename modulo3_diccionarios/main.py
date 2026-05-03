# 1. Definición de ventas_por_region como dict anidado
ventas_por_region = {
    "Norte": {"Q1": 15000, "Q2": 18000, "Q3": 12000, "Q4": 20000},
    "Sur":   {"Q1": 22000, "Q2": 25000, "Q3": 28000, "Q4": 30000},
    "Este":  {"Q1": 10000, "Q2": 11000, "Q3": 9500,  "Q4": 13000},
    "Oeste": {"Q1": 19000, "Q2": 17000, "Q3": 21000, "Q4": 18500}
}

# 2. Calcula el total anual de cada región con items() y sum(values())
totales_anuales = {region: sum(trimestres.values()) for region, trimestres in ventas_por_region.items()}

# 3. Usa max() con key=lambda para la región con mayores ventas
mejor_region = max(totales_anuales.items(), key=lambda x: x[1])

# 4. Acumula ventas por trimestre con iteración anidada
ventas_trimestrales = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}
for trimestres in ventas_por_region.values():
    for q, monto in trimestres.items():
        ventas_trimestrales[q] += monto

# 5. Genera porcentajes con dict comprehension sobre el gran total
gran_total = sum(totales_anuales.values())
porcentajes = {region: (total / gran_total) * 100 for region, total in totales_anuales.items()}

# 6. Imprime reporte ordenado de mayor a menor con sorted() + items()
print(f"{'REGIÓN':<10} | {'TOTAL':<10} | {'PORCENTAJE':<10}")
print("-" * 35)

reporte_ordenado = sorted(totales_anuales.items(), key=lambda x: x[1], reverse=True)

for region, total in reporte_ordenado:
    pct = porcentajes[region]
    print(f"{region:<10} | ${total:<9,} | {pct:>8.2f}%")

print("-" * 35)
print(f"La región con mejores ventas fue: {mejor_region[0]} (${mejor_region[1]:,})")