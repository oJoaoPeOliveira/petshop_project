from funcionario import Funcionario

class Veterinario(Funcionario):
    def __init__(self, nome, cpf, telefone, email, salario, crmv):
        super().__init__(nome, cpf, telefone, email, salario)
        self._crmv = crmv
        
        self._ativo = True
        
    def __str__(self):
        return f'{super.__str__()} - CRMV: {self._crmv}'