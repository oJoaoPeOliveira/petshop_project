from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, idade, raca):
        self._nome = nome
        self._idade = idade
        self._raca = raca
        
        self._responsavel = None
        self._tipo_sanguineo = None
        
    def __str__(self):
        return 'Oi'
    
    @property
    def responsavel(self):
        return self._responsavel
    
    def atribuir_responsavel(self, responsavel):
        self._responsavel = responsavel
        
    @property
    def tipo_sanguineo(self):
        return self._tipo_sanguineo
    
    def registrar_tipo_sanguineo(self, tipo):
        self._tipo_sanguineo = tipo
        
    @abstractmethod
    def emitir_som(self):
        return 'Som genérico'