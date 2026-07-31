print("--- CALCULADORA DE CALIFICACIONES FINALES ---")

# Entrada de datos
parciales = float(input("Ingresa la nota promedio de parciales (0-100): "))
proyecto = float(input("Ingresa la nota del proyecto (0-100): "))
examen = float(input("Ingresa la nota del examen final (0-100): "))

# Cálculo ponderado
calificacion_final = (parciales * 0.40) + (proyecto * 0.30) + (examen * 0.30)

# Mostrar resultado
print(f"\nCalificación Final: {calificacion_final:.2f}")

input("\nPresiona Enter para salir...")