def byte_representation(char):
    """ Retorna la representación en byte de un único carácter o palabra. """
    return ' '.join(format(ord(c), '08b') for c in char)

def ascii_representation(byte_str):
    """ Retorna el carácter ASCII de una cadena de byte. """
    char = chr(int(byte_str, 2))
    return f'{char}-{ord(char)}'

def main():
    while True:
        print("\nMenú de opciones:")
        print("1. Representación en byte de un carácter o palabra")
        print("2. Generar la representación ASCII de un byte")
        print("3. Salir")
        choice = input("Ingrese su elección: ")

        if choice == '1':
            char = input("Ingrese un carácter o palabra: ")
            print("Representación en byte:", byte_representation(char))
        elif choice == '2':
            byte_str = input("Ingrese una secuencia de bytes: ")
            print("Representación ASCII:", ascii_representation(byte_str))
        elif choice == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor intente de nuevo.")

if __name__ == "__main__":
    main()
