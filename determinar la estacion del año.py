print("--- ESTACIÓN DEL AÑO ---")

mes = input("Ingresa un mes del año: ").strip().lower()

match mes:
    case "diciembre" | "enero" | "febrero":
        estacion = "Invierno"
    case "marzo" | "abril" | "mayo":
        estacion = "Primavera"
    case "junio" | "julio" | "agosto":
        estacion = "Verano"
    case "septiembre" | "octubre" | "noviembre":
        estacion = "Otoño"
    case _:
        estacion = "Mes no válido"

print(f"\nPara el mes de '{mes.capitalize()}', la estación es: {estacion}")

input("\nPresiona Enter para salir...")