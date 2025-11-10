from modelos.animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        """
        Inicializa uma instância de Cachorro
        
        Inputs:
        - nome (str): O nome do cachorro
        - idade (float): A idade do cachorro
        - raca (str): A raça do cachorro
        """
        super().__init__(nome, idade, raca)
        
    def __str__(self):
        """
        Retorna uma representação em string do cachorro
        
        Outputs:
        - str: O nome, raça e idade do cachorro
        """
        return f'{super().__str__()}'
    
    def emitir_som(self):
        """
        Essa função emite o som do cachorro
        
        Outputs:
            tipo (str): O latido do cachorro
        """
        return 'Au Au Au!'
    