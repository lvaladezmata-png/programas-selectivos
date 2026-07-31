print("--- CÁLCULO DE DESCUENTOS ---")

precio_original = float(input("Ingresa el precio del producto/compra: $"))

if precio_original <= 100:
    descuento_pct = 0
elif precio_original <= 200:
    descuento_pct = 5    # 5% de descuento
elif precio_original <= 500:
    descuento_pct = 10   # 10% de descuento
else:
    descuento_pct = 15   # 15% de descuento

monto_descuento = precio_original * (descuento_pct / 100)
precio_final = precio_original - monto_descuento

print(f"\nPorcentaje de descuento aplicado: {descuento_pct}%")
print(f"Monto descontado: ${monto_descuento:.2f}")
print(f"Precio final a pagar: ${precio_final:.2f}")

input("\nPresiona Enter para salir...")
