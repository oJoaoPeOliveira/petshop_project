from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, idade, raca):
        """
        Inicializa uma instância de Animal
        
        Inputs:
        - nome (str): O nome do animal
        - idade (float): A idade do animal
        - raca (str): A raça do animal
        """
        self._nome = nome
        self._idade = idade
        self._raca = raca
        
        self._responsavel = None
        self._tipo_sanguineo = None
        
    def __str__(self):
        """
        Retorna uma representação em string do restaurante
        
        Outputs:
        - str: O nome, raça e idade do animal
        """
        return f'{self._nome} ({self._raca}) - {self._idade} anos'
    
    @property
    def responsavel(self):
        """
        Essa função retorna o nome do responsável do animal
        
        Outputs:
            str: O nome do responsável do animal
        """
        return self._responsavel
    
    def atribuir_responsavel(self, responsavel):
        """
        Essa função atribui o nome do responsável do animal
        
        Inputs:
            responsavel (str): O nome do responsável do animal
        """
        self._responsavel = responsavel
        
    @property
    def tipo_sanguineo(self):
        """
        Essa função retorna o tipo sanguineo do animal
        
        Outputs:
            str: O tipo sanguineo do animal
        """
        return self._tipo_sanguineo
    
    def registrar_tipo_sanguineo(self, tipo):
        """
        Essa função atribui o tipo sanguineo do animal
        
        Inputs:
            tipo (str): O tipo sanguineo do animal
        """
        self._tipo_sanguineo = tipo
        
    @abstractmethod
    def emitir_som(self):
        """
        Essa função emite o som do animal
        
        Outputs:
            tipo (str): O som do animal
        """
        return 'Som genérico'