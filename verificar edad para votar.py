print("--- VERIFICACIÓN DE EDAD PARA VOTAR ---")

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("\n✓ Eres mayor de edad. ¡Puedes votar!")
elif edad >= 0:
    print(f"\n✗ Tienes {edad} años. No puedes votar aún (requieres 18 años).")
else:
    print("\nEdad no válida.")

input("\nPresiona Enter para salir...")