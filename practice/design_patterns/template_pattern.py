from abc import ABC, abstractmethod

class MakeCake(ABC):
    def __init__(self):
        self.prepara_masa()
        self.hornear(45)
    
    def prepara_masa(self):
        print('Tamizar la harina')
        print('Agregar dos huevos')
        print('etc')

    def hornear(self, grado):
        print(f'Poner el pastel en un horno a {grado} grados')
        print('Saca el pastel cuando este listo')


class MakeChocaleCake(MakeCake):
    def prepara_masa(self):
        print('Agregra chocolate')

class MakeVainallaCake(MakeCake):
    def prepara_masa(self):
        print('Agregar vainilla')


if __name__ == '__main__':
    MakeCake()
    MakeChocaleCake()
    MakeVainallaCake()