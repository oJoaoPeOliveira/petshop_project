from modelos.animal import Animal
from modelos.cliente import Cliente
from modelos.veterinario import Veterinario

class Consulta:
    def __init__(self, animal, cliente, veterinario, data: str, hora_inicio: str, hora_fim: str, valor: float, detalhes_da_consulta: str = ''):
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
        
        self._detalhes_da_consulta = detalhes_da_consulta
        self._data = data
        self._hora_inicio = hora_inicio
        self._hora_fim = hora_fim
        self._valor = valor

        self._status = False
        self._diagnostico = None
        self._pago = False
        
    def __str__(self):
        return f'{self._animal}'
    
    def finalizar_consulta(self, diagnostico: str):
        """
            Registra o diagnóstico final e encerra a consulta
            
            Inputs: 
            - diagnostico (str): Diagnóstico final do atendimento
            
            Outputs:
            - str: Confirmação da realização da consulta ou que está ativa ainda
        """
        if not self._status:
            self._diagnostico = diagnostico
            self._status = True
            
            return 'Consulta realizada com sucesso'
    
        else:
            return 'Consulta ainda não foi finalizada'
        
    def registrar_pagamento(self):
        """
            Está função define o pagamento da consulta foi realizado
            
            Outputs:
            - str: Status da consulta ativa ou pagamento da consulta
        """
        if self._status:
            if not self._pago:
                self._pago = True
                return 'O Pagamento foi realizado com sucesso'
            else:
                return 'A conta já está paga'
        else:
            return 'A consulta só pode ser paga após finalizada'