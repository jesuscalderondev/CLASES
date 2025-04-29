class Shape:

    def calculate_perimeter(self) -> float:
        pass

    def calculate_area(self) -> float:
        pass
    
class Circle(Shape):

    def __init__(self, radius: float): # metodo constructor
        self.radius = radius
    
    def calculate_perimeter(self) -> float:
        return 2 * 3.1415 * self.radius
    
    def calculate_area(self) -> float:
        return 3.1415 * self.radius ** 2

class Square(Shape):

    def __init__(self, side: float):
        self.side = side

    def calculate_perimeter(self) -> float:
        return self.side * 4
    
    def calculate_area(self) -> float:
        return self.side ** 2
    
class Rectangle(Shape):

    def __init__(self, width: float, long: float):
        self.width = width
        self.long = long

    def calculate_perimeter(self) -> float:
        return self.width * 2 + self.long * 2
    
    def calculate_area(self) -> float:
        return self.width * self.long  # base * altura
    


#EJEMPLOS DE HERENCIA MULTIPLE

""" Si tenemos la clase Computer que tiene
* Processor
* RAM
* Hard drive
* Video card (En algunos casos)
* Socket

"""

class Processor:

    def __init__(self, model_processor:str, cores: int, threads: int, frequency_processor: float, architecture: str, cache: str, brand_processor: str):
        self.model_processor = model_processor
        self.cores = cores
        self.threads = threads
        self.frequency_processor = frequency_processor
        self.architecture = architecture
        self.cache = cache
        self.brand_processor = brand_processor
        

class Ram:

    def __init__(self, model_ram: str, frequency_ram: float, capacity_ram: int, brand_ram: str, generation_ram: str):
        self.model_ram = model_ram
        self.frequency_ram = frequency_ram
        self.capacity_ram = capacity_ram
        self.brand_ram = brand_ram
        self.generation_ram = generation_ram

class HardDrive:

    def __init__(self, model_hard: str, capacity_hard: int, type_hard: str):
        self.model_hard = model_hard
        self.capacity_hard = capacity_hard
        self.type_hard = type_hard

class Socket:

    def __init__(self, color: str, dimensions: str):
        self.color = color
        self.dimensions = dimensions

class Computer(Processor, Ram, HardDrive, Socket):

    def __init__(self, model_processor, cores, threads, frequency_processor, architecture, cache, brand_processor, model_ram, frequency_ram, capacity_ram, brand_ram, generation_ram, model_hard, capacity_ram_hard, type_ram_hard, color, dimensions):
        Processor.__init__(self, model_processor, cores, threads, frequency_processor, architecture, cache, brand_processor)
        Ram.__init__(self, model_ram, frequency_ram, capacity_ram, brand_ram, generation_ram)
        HardDrive.__init__(self, model_hard, capacity_ram_hard, type_ram_hard)
        Socket.__init__(self, color, dimensions)