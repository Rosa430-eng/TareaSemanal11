import json
import os
from modelo.mascota import Mascota


class GestionVeterinaria:
    def __init__(self, archivo="mascotas.json"):
        self.archivo = archivo
        self.mascotas = {}  # diccionario
        self.cargar()

    def agregar_mascota(self, mascota):
        if mascota.get_id() in self.mascotas:
            print(" Ya existe.")
        else:
            self.mascotas[mascota.get_id()] = mascota
            print(" Mascota registrada.")
            self.guardar()

    def eliminar_mascota(self, id_mascota):
        if id_mascota in self.mascotas:
            del self.mascotas[id_mascota]
            print(" Eliminada.")
            self.guardar()
        else:
            print(" No encontrada.")

    def atender_mascota(self, id_mascota):
        if id_mascota in self.mascotas:
            self.mascotas[id_mascota].set_estado("Atendido")
            print(" Mascota atendida.")
            self.guardar()
        else:
            print(" No encontrada.")

    def buscar_por_dueno(self, dueno):
        resultados = [
            m for m in self.mascotas.values()
            if dueno.lower() in m.get_dueno().lower()
        ]

        if resultados:
            for m in resultados:
                print(m)
        else:
            print(" No hay resultados.")

    def mostrar_todas(self):
        if not self.mascotas:
            print(" Sin registros.")
        else:
            for m in self.mascotas.values():
                print(m)

    # ARCHIVOS
    def guardar(self):
        data = [m.to_dict() for m in self.mascotas.values()]
        with open(self.archivo, "w") as f:
            json.dump(data, f, indent=4)

    def cargar(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                try:
                    data = json.load(f)
                    for item in data:
                        mascota = Mascota.from_dict(item)
                        self.mascotas[mascota.get_id()] = mascota
                except:
                    self.mascotas = {}