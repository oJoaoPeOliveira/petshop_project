class Cliente:
    
    def __init__(self, nome, cpf, telefone, cep):
        """
        Inicializa uma instância de Cliente
        
        Inputs:
        - nome (str): O nome do cliente
        - cpf (str): O cpf do cliente
        - telefone (str): O telefone do cliente
        - cep (str): O cep do cliente
        """
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
        self._cep = cep
        
        self._pets = []
        self._ativo = True
    
    def adicionar_pet(self, animal):
        """
        Adiciona uma instância do animal ao responsável
        
        Inputs:
        - animal (Animal): O cachorro ou gato
        """
        self._pets.append(animal)
    
    @property
    def ativo(self):
        """
        Retorna se está ativo ou não em forma de texto
        
        Outputs:
        - str: O status do cliente
        """
        return 'Ativado' if self._ativo else 'Desativado'
    
    def alternar_estado(self):
        """ Altera o estado do status do cliente """
        self._ativo = not self._ativo
    
    def __str__(self):
        """
        Retorna uma representação em string do cliente
        
        Outputs:
        - str: O nome, cpf, status e quantidade de animais que o cliente tem na clinica ou pet
        """
        numero_pets = len(self._pets)
        return f'Cliente: {self._nome} CPF: {self._cpf} | Status: {self.ativo} | Pets: {numero_pets}'