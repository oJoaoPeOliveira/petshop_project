from modelos.animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade, raca)
        
    def __str__(self):
        return f'{super().__str__()}'
    
    def emitir_som(self):
        return 'Au Au Au!'
    