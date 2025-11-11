class Consulta:
    def __init__(self, animal, cliente, veterinario, data: str, hora_inicio: str, hora_fim: str, valor: float, detalhes_agendamento: str = ''):
        """
        Inicializa uma instância de Funcionario
        
        Inputs:
        - animal (Animal): Instância da classe Gato ou Cachorro
        - cliente (Cliente): Instância da classe Cliente
        - veterinario (veterinario): Instância da classe Veterinario
        - hora_inicio (str): Horário inicial do atendimento
        - hora_fim (str): Horário final do atendimento
        - valor (float): Valor da consulta
        - detalhes_agendamento (str): Motivo da consulta
        """
        self._animal = animal
        self._cliente = cliente
        self._veterinario = veterinario
        
        self._data = data
        self._detalhes_agendamento = detalhes_agendamento
        self._hora_inicio = hora_inicio
        self._hora_fim = hora_fim 
        self._valor = valor

        self._detalhes_da_consulta = ''
        self._status = True
        self._diagnostico = None
        self._pago = False