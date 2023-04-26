from enum import Enum

class Visibilidade(Enum):
    PUBLICO = 0
    PRIVADO = 1
    
    def get_visibility(codigo):
        if codigo == 1:
            return Visibilidade.PRIVADO
        return Visibilidade.PUBLICO
        
    def get_value(name):
        if name == "PRIVADO":
            return 1
        return 0