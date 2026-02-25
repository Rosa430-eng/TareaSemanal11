class Mascota:
    def __init__(self, id_mascota, nombre, especie, dueno, estado="Pendiente"):
        self._id = id_mascota
        self._nombre = nombre
        self._especie = especie
        self._dueno = dueno
        self._estado = estado

    # GETTERS
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_especie(self):
        return self._especie

    def get_dueno(self):
        return self._dueno

    def get_estado(self):
        return self._estado

    # SETTERS
    def set_estado(self, estado):
        self._estado = estado

    def set_nombre(self, nombre):
        self._nombre = nombre

    def to_dict(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "especie": self._especie,
            "dueno": self._dueno,
            "estado": self._estado
        }

    @staticmethod
    def from_dict(data):
        return Mascota(
            data["id"],
            data["nombre"],
            data["especie"],
            data["dueno"],
            data["estado"]
        )
        
    def __str__(self):

        return f"ID:{self._id} | {self._nombre} ({self._especie}) | Dueño: {self._dueno} | Estado: {self._estado}"

