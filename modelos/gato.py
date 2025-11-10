from modelos.animal import Animal

class Gato(Animal):
    def __init__(self, nome, idade, raca):
        """
        Inicializa uma instância de Gato
        
        Inputs:
        - nome (str): O nome do gato
        - idade (float): A idade do gato
        - raca (str): A raça do gato
        """
        super().__init__(nome, idade, raca)
        
    def __str__(self):
        """
        Retorna uma representação em string do gato
        
        Outputs:
        - str: O nome, raça e idade do gato
        """
        return f'{super().__str__()}'
    
    def emitir_som(self):
        """
        Essa função emite o som do gato
        
        Outputs:
            tipo (str): O miado do gato
        """
        return 'Miau Miau Miau!'