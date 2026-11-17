from abc import ABC, abstractmethod
from datetime import datetime

#Importa excecoes personalizado para saldo insuficiente
from utilitarios.exceptions import SaldoInsuficientError


#Define a classe abstrata conta, que serve como base para outros tipos de conta
class Conta(ABC):

  """
  Calasse base abstrata para conta bancárias
  Herança e Encapsulamento.
  """

  _total_contas = 0

  #Metodo construtor que inicia o atributo da classe
  def __init__(self, numero: int, cliente):

    #Numero da conta, atributo protegido
    self._numero = numero

    #Saldo da conta, inicializado cem 0.0 (atributo protegido)
    self._saldo = 0.0

    #Referencia ao cliente dono da conta
    self._Cliente = cliente

    #Lista par armazenar histórico de transacoes
    self._historico = []

    Conta._total_contas += 1

  #Propriedade para acessar o saldo de forma controlada
  @property
  def saldo(self):
    """Getter para o saldo, permitindo acesso controlado """
    return self.saldo

  #Metodo de classe para consultar o numero total de contas
  @classmethod
  def get_total_contas(cls):
    """Metodo de classe para obter o numero total de contas criadas"""
    return cls._total_contas

  #Metodo para realisar depositos
  def depositar(self, valor: float):

    #Adiciona um valor ao saldo da conta
    if valor > 0:

      #Incrementa o saldo
      self._saldo += valor

      #Registra a transação no historico com data e hora
      self._historico.append((datetime.now(), f"Depósito de R${valor:.2f}"))
      print(f"Depósito de R${valor:.2f} realizado com sucesso")

    else:
      print("Valor de desótio inválido")
  
  #Metdodo abstrato que deve ser implementado pelas subclasses
  @abstractmethod
  def sacar(self, valor: float):
    """Metodo abstrato para sacar um valor, deve ser implementado pelas subclasses"""
    pass

#Metodo para exibir o extrato da conta
  def extrato(self):
    """Exibe o extrato da conta"""
    print(f"\n ---Extrato da Conta N° {self._nuero} ---")
    print(f"Cliente: {self._Cliente}")
    print(f"Saldo atual da R$:{self._saldo:.2f}")
    print(f"Histórico de Transações:")

    #Caso não haja transações registradas
    if not self._historico:
      print("Nenhuma trasação registrada.")

    for data, transacao in self._historico:
      print(f"- {data.strftime('%d/%m/%Y %H:%M:%S')}: {transacao}")
    print("----------------------------------\n") 

#Define a subclasse ContaCorrente
# class ContaCorrente(Conta):