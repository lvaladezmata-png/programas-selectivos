print("--- CONVERSOR DE MONEDAS DESDE PESOS MEXICANOS (MXN) ---")

mxn = float(input("Ingresa la cantidad en pesos mexicanos (MXN): $"))

print("\nOpciones de conversión disponibles:")
print("USD - Dólar Estadounidense   EUR - Euro                 THB - Baht Tailandés")
print("JPY - Yen Japonés            KRW - Won Surcoreano        AUD - Dólar Australiano")
print("PEN - Sol Peruano            CAD - Dólar Canadiense      VES - Bolívar Venezolano")
print("ARS - Peso Argentino")

destino = input("\nIngresa el código de la moneda a convertir: ").strip().upper()

# Tasas de cambio aproximadas de referencia respecto al MXN
match destino:
    case "USD":
        conversion = mxn * 0.055
        print(f"\n${mxn:.2f} MXN equivale a ${conversion:.2f} USD")
    case "EUR":
        conversion = mxn * 0.051
        print(f"\n${mxn:.2f} MXN equivale a €{conversion:.2f} EUR")
    case "THB":
        conversion = mxn * 1.98
        print(f"\n${mxn:.2f} MXN equivale a ฿{conversion:.2f} THB")
    case "JPY":
        conversion = mxn * 8.52
        print(f"\n${mxn:.2f} MXN equivale a ¥{conversion:.2f} JPY")
    case "KRW":
        conversion = mxn * 76.50
        print(f"\n${mxn:.2f} MXN equivale a ₩{conversion:.2f} KRW")
    case "AUD":
        conversion = mxn * 0.083
        print(f"\n${mxn:.2f} MXN equivale a A${conversion:.2f} AUD")
    case "PEN":
        conversion = mxn * 0.20
        print(f"\n${mxn:.2f} MXN equivale a S/{conversion:.2f} PEN")
    case "CAD":
        conversion = mxn * 0.075
        print(f"\n${mxn:.2f} MXN equivale a C${conversion:.2f} CAD")
    case "VES":
        conversion = mxn * 2.01
        print(f"\n${mxn:.2f} MXN equivale a Bs.{conversion:.2f} VES")
    case "ARS":
        conversion = mxn * 52.30
        print(f"\n${mxn:.2f} MXN equivale a ${conversion:.2f} ARS")
    case _:
        print("\nMoneda no soportada o código incorrecto.")

input("\nPresiona Enter para salir...")