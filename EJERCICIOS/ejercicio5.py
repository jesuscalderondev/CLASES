#EJEMPLO DE MÉTODOS ESTÁTICOS

class Mascota:

    #A las declaraciones como estas que están en las cabeceras se le llaman atributos de clase
    nombre = None

    def __init__(self, nombre:str, edad:int, especie:str, sexo:str, amo:str):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.sexo = sexo
        self.amo = amo
    
    
    @classmethod
    def mostrarDatosDeMascota(self):
        print(f'Los datos de la mascota son: {self.nombre}, {self.edad}, {self.especie}, {self.sexo}, {self.amo}')

    def actualizarEdad(self, edad: int):

        if edad != self.edad:
            self.edad = edad
        print(f'La nueva edad es: {self.edad}')

    def actualizarNombre(self, nombre: str):

        if nombre != self.nombre:
            self.nombre = nombre
        print(f'El nuevo nombre es: {self.nombre}')

    def actualizarEspecie(self, especie: str):

        if especie != self.especie:
            self.especie = especie
        print(f' La nueva especie es: {self.especie}')

    #Se le conoce como método estático
    @staticmethod
    def imprirTexto(text:str) -> None:
        print(text)

    def imprimirNombre(self) -> None:
        print(self.nombre)


#EJEMPLO DE HERENCIA 

class Persona:

    def __init__(self, nombre: str, edad: int, colorDePiel: str, sexo: str, estatura: float, peso: float):
        self.nombre = nombre
        self.edad = edad
        self.colorDePiel = colorDePiel
        self.sexo = sexo
        self.estatura = estatura
        self.peso = peso

    def caminar(self):
        pass

    def correr(self):
        pass

    def presentar(self):
        print(f"Mucho gusto, mi nombre es {self.nombre}")
    
    def despedir(self, nombreDeLaOtrPersona:str):
        print(f"Hasta luego, {nombreDeLaOtrPersona}")

class Colombiano(Persona):
    pass

class EstadoUnidense(Persona):

    def presentar(self):
        print(f"Hi, my name is {self.nombre}")

    def despedir(self, nombreDeLaOtraPersona:str):
        print(f"Bye, {nombreDeLaOtraPersona}")

col = Colombiano(
    "Juan Pepito",
    25,
    "Morena",
    "M",
    1.85,
    84.9
)

eeuu = EstadoUnidense(
    "Kyle Smith",
    28,
    "Blanco",
    "M",
    1.95,
    100
)

eeuu.presentar()
col.presentar()
eeuu.despedir(col.nombre)
col.despedir(eeuu.nombre)

#EJEMPLO DE HERENCIA #2
class Vehiculo:

    def __init__(self, color: str, modelo: int, ruedas: int, ancho: float, largo: float, altura: float, asientos: int):
        self.color = color
        self.modelo = modelo
        self.ruedas= ruedas
        self.ancho = ancho
        self.largo = largo
        self.altura = altura
        self.asientos = asientos

class Carro(Vehiculo):

    def __init__(self, color, modelo, ruedas, ancho, largo, altura, asientos, placa:str):
        super().__init__(color, modelo, ruedas, ancho, largo, altura, asientos)
        self.placa = placa

class Avion(Vehiculo):

    def volar(self):
        print("Está volando")

class Bote(Vehiculo):

    def __init__(self, color, modelo, ruedas, ancho, largo, altura, asientos, remos: int):
        super().__init__(color, modelo, ruedas, ancho, largo, altura, asientos)
        self.remos = remos
