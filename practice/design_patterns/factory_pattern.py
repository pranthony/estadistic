from abc import ABC, abstractmethod
from enum import Enum

class Furniture(ABC):
    @abstractmethod
    def ensable(self):
        pass

class Table(Furniture):
    def ensable(self):
        return 'Ensambling table'

class  Chair(Furniture):
    def ensable(self):
        return 'Ensambilng chair'
    

class FuritureType(Enum):
    TABLE = 'table'
    CHAIR = 'chair'

class FactoryFuriture(Furniture):
    def __init__(self):
        self.furitures = {
            FuritureType.TABLE: Table(),
            FuritureType.CHAIR: Chair()
        }

    def ensable(self, feature_type):
        return self.furitures[feature_type].ensable()

if __name__ == "__main__":
    furniture = FactoryFuriture()
    table = furniture.ensable(FuritureType.TABLE)
    print(table)
    chair = furniture.ensable(FuritureType.CHAIR)
    print(chair)
    