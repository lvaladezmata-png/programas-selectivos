print("--- EVALUACIÓN DE CALIFICACIONES CON LETRAS ---")

nota = float(input("Ingresa tu calificación (0 - 100): "))

if 90 <= nota <= 100:
    letra = "A (Excelente)"
elif 80 <= nota < 90:
    letra = "B (Bueno)"
elif 70 <= nota < 80:
    letra = "C (Regular)"
elif 60 <= nota < 70:
    letra = "D (Suficiente)"
elif 0 <= nota < 60:
    letra = "F (Reprobado)"
else:
    letra = "Calificación fuera de rango"

print(f"\nTu evaluación es: {letra}")

input("\nPresiona Enter para salir...")