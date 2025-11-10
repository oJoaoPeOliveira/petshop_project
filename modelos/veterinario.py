from funcionario import Funcionario

class Veterinario(Funcionario):
    def __init__(self, nome, cpf, telefone, email, salario, crmv):
        """
        Inicializa uma instância de Funcionario
        
        Inputs:
        - nome (str): O nome do veterinário
        - cpf (str): O cpf do veterinário
        - telefone (str): O telefone do veterinário
        - email (str): O email do veterinário
        - salario (float): O valor do salário do veterinário
        - crmv (str): O número do registro do CRMV do veterinário
        """
        super().__init__(nome, cpf, telefone, email, salario)
        self._crmv = crmv
        
        self._ativo = True
        
    def __str__(self):
        """
        Retorna uma representação em string do funcionário
        
        Outputs:
        - str: O nome, e-mail e CRMV do veterinário
        """
        return f'{super.__str__()} - CRMV: {self._crmv}'