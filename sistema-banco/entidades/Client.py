#Criando a classe Cliente
class Client:

  #Metodo construtor que inicia o atributo da classe
  def __init__(self, nome: str, cpf: str):

    #Criando o atiburo nome, para cliente receber um nome
    self.nome = nome

    #Criando o atributo cpf, pois todo cliente tem um cpf
    self.cpf = cpf

    #Lista par armazenar os cliente associados a uma conta.
    self.conta = []


  #Metedo para adicionar uma conta a lista vazia de contas.
  def Criar_conta(self, conta):

    #Insere o objeto como lista em contas
    self.contas.append(conta)


  #Metodo especial que define a representacao em string do objeto
  def __str__(self):

    #String formatada com nome e cpf do Cliente
    return f"Cliente: {self.nome} (CPF:{self.cpf})"