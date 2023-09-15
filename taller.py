from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False

@dataclass
class Conjunto:
    elementos: list = []
    nombre: str = ""
    contador: int = 0

    def __post_init__(self):
        Conjunto.contador += 1
        self.__id = Conjunto.contador

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento):
        return any(e == elemento for e in self.elementos)

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        if isinstance(otro_conjunto, Conjunto):
            for elemento in otro_conjunto.elementos:
                self.agregar_elemento(elemento)

    def __add__(self, otro_conjunto):
        nuevo_conjunto = Conjunto(self.nombre)
        nuevo_conjunto.elementos = self.elementos.copy()
        nuevo_conjunto.unir(otro_conjunto)
        return nuevo_conjunto

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        if isinstance(conjunto1, Conjunto) and isinstance(conjunto2, Conjunto):
            elementos_comunes = [elemento for elemento in conjunto1.elementos if conjunto2.contiene(elemento)]
            nombre_resultado = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
            return cls(elementos_comunes, nombre_resultado)

    def __str__(self):
        elementos_str = ", ".join(str(elemento.nombre) for elemento in self.elementos)
        return f"Conjunto {self.nombre}: ({elementos_str})"

elemento1 = Elemento("A")
elemento2 = Elemento("B")
elemento3 = Elemento("C")


conjunto1 = Conjunto("Conjunto1")
conjunto2 = Conjunto("Conjunto2")


conjunto1.agregar_elemento(elemento1)
conjunto1.agregar_elemento(elemento2)
conjunto2.agregar_elemento(elemento2)
conjunto2.agregar_elemento(elemento3)


union = conjunto1 + conjunto2
print(union)

interseccion = Conjunto.intersectar(conjunto1, conjunto2)
print(interseccion)