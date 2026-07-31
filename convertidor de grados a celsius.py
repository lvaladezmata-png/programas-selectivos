print("--- CONVERTIDOR DE TEMPERATURA ---")

celsius = float(input("Ingresa los grados Celsius (°C): "))

print("\n¿A qué unidad deseas convertir?")
print("1. Fahrenheit")
print("2. Kelvin")
opcion = input("Elige una opción (1 o 2): ").strip()

match opcion:
    case "1" | "fahrenheit" | "Fahrenheit":
        resultado = (celsius * 9/5) + 32
        print(f"\n{celsius}°C equivalen a {resultado:.2f}°F")
    case "2" | "kelvin" | "Kelvin":
        resultado = celsius + 273.15
        print(f"\n{celsius}°C equivalen a {resultado:.2f} K")
    case _:
        print("\nOpción no válida.")

input("\nPresiona Enter para salir...")