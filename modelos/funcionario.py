class Funcionario:
    def __init__(self, nome, cpf, telefone, email, salario):
        """
        Inicializa uma instância de Funcionario
        
        Inputs:
        - nome (str): O nome do funcionário
        - cpf (str): O cpf do funcionário
        - telefone (str): O telefone do funcionário
        - email (str): O email do funcionário
        - salario (float): O valor do salário do funcionário
        """
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
        self._email = email
        self._salario = salario
        
        self._ativo = True
        
    def __str__(self):
        """
        Retorna uma representação em string do funcionário
        
        Outputs:
        - str: O nome e o e-mail do funcionário
        """
        return f'{self._nome} - {self._email}'