from servicios.gestion_veterinaria import GestionVeterinaria
from modelo.mascota import Mascota


def menu():
    print("\n===== VETERINARIA =====")
    print("1. Registrar mascota")
    print("2. Eliminar mascota")
    print("3. Atender mascota")
    print("4. Buscar por dueño")
    print("5. Mostrar todas")
    print("6. Salir")


def main():
    sistema = GestionVeterinaria()

    while True:
        menu()
        op = input("Opción: ")

        if op == "1":
            id_m = input("ID: ")
            nombre = input("Nombre: ")
            especie = input("Especie: ")
            dueno = input("Dueño: ")

            mascota = Mascota(id_m, nombre, especie, dueno)
            sistema.agregar_mascota(mascota)

        elif op == "2":
            sistema.eliminar_mascota(input("ID: "))

        elif op == "3":
            sistema.atender_mascota(input("ID: "))

        elif op == "4":
            sistema.buscar_por_dueno(input("Dueño: "))

        elif op == "5":
            sistema.mostrar_todas()

        elif op == "6":
            break

        else:
            print(" Opción inválida")


if __name__ == "__main__":
    main()