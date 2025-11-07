from modelos.animal import Animal

class Gato(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade, raca)
        
    def __str__():
        pass
    
    def emitir_som(self):
        return 'Miau Miau Miau!'