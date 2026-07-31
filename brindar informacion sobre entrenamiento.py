print("--- CENTRO DE INFORMACIÓN DE ENTRETENIMIENTO ---")
print("1. Queen (Artista)")
print("2. Interstellar (Película)")
print("3. Breaking Bad (Serie)")
print("4. Taylor Swift (Artista)")
print("5. Stranger Things (Serie)")

opcion = input("\nIngresa el número o nombre de la opción para ver su información: ").strip().lower()

match opcion:
    case "1" | "queen":
        print("\n[ARTISTA] Queen")
        print("• Género: Rock")
        print("• Origen: Reino Unido (1970)")
        print("• Miembros icónicos: Freddie Mercury, Brian May, Roger Taylor, John Deacon.")
        print("• Canciones famosas: 'Bohemian Rhapsody', 'Don't Stop Me Now', 'We Will Rock You'.")

    case "2" | "interstellar":
        print("\n[PELÍCULA] Interstellar")
        print("• Director: Christopher Nolan")
        print("• Año: 2014")
        print("• Género: Ciencia Ficción / Drama espacial")
        print("• SINOPSIS: Un grupo de astronautas viaja a través de un agujero de gusano en busca de un nuevo hogar para la humanidad.")

    case "3" | "breaking bad":
        print("\n[SERIE] Breaking Bad")
        print("• Creador: Vince Gilligan")
        print("• Temporadas: 5")
        print("• Género: Drama criminal / Thriller")
        print("• SINOPSIS: Un profesor de química diagnosticado con cáncer se alía con un exalumno para fabricar sustancia ilícita y asegurar el futuro financiero de su familia.")

    case "4" | "taylor swift":
        print("\n[ARTISTA] Taylor Swift")
        print("• Género: Pop / Country / Folk")
        print("• Origen: Estados Unidos")
        print("• Álbumes destacados: '1989', 'Folklore', 'Midnights'.")
        print("• Logro: Una de las artistas con más premios Grammy al Álbum del Año.")

    case "5" | "stranger things":
        print("\n[SERIE] Stranger Things")
        print("• Creadores: Hermanos Duffer")
        print("• Género: Ciencia Ficción / Fantasía / Terror")
        print("• SINOPSIS: En la década de 1980, la desaparición de un niño en un pequeño pueblo destapa misterios del gobierno y fuerzas sobrenaturales.")

    case _:
        print("\nNo se encontró información para la opción seleccionada.")

input("\nPresiona Enter para salir...")