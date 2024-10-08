from abc import ABC, abstractmethod

class MakePapper(ABC):
    def __init__(self):
        # Aqui se ejecutaran todos los contenidos de un papper
        pass

    def core_topic(self):
        pass    
    
    def make_title(self):
        return 'El titulo debe contener maximo 18 palabras'
    
    def references(self):
        return 'Las referencias deben estar en formato APA 7ma edición'

    def make_abstract(self):
        return 'Redactar el resumen en un maximo de 300 palabras, el resemen debe contener el planteamiento del problema, principal obetivo, metodología, principal resultado y principal conclusión'
    
    def make_key_words(self):
        return 'Elegir 5 palabras clave que describan las investigación aprobadas por thesauros de la UNESCO'
    
    