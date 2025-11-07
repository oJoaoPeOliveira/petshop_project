class Cliente:
    
    def __init__(self, nome, cpf, telefone, cep):
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
        self._cep = cep
        
        self._pets = []
        self._ativo = True
    
    def adicionar_pet(self, animal):
        self._pets.append(animal)
    
    @property
    def ativo(self):
        return 'Ativado' if self._ativo else 'Desativado'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
    
    def __str__(self):
        numero_pets = len(self._pets)
        return f'Cliente: {self._nome} CPF: {self._cpf} | Status: {self.ativo} | Pets: {numero_pets}'