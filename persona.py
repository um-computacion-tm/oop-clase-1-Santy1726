
class Persona:
    

    def __init__(self, nombre: str = 'Santiago' , apellido: str = 'Ortega' , du: int = '14725836'):               #du = documento
        self.__nombre__= nombre
        self.__apellido__ = apellido
        self.__du__ = du


    def mostrar_datos(self):
        print(f'Mis datos son nombre = {self.__nombre__} apellido = {self.__apellido__} documento = {self.__du__}')






