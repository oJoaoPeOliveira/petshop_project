class Funcionario:
    def __init__(self, nome, cpf, telefone, email, salario):
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
        self._email = email
        self._salario = salario
        
        self._ativo = True
        
    def __str__(self):
        return f'{self._nome} - {self._email}'