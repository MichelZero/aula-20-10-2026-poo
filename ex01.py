# autor: Michel
# data: 20/10/2026

class Termometro:
  # parte 1: o Construtor 
  def __init__(self, temp_inicial = 25.0):
    self._temperatura = temp_inicial
    self.campo2 = 0
    
  # get
  @property
  def temperatura(self):
    return self._temperatura
  
  @property
  def campo2(self):
    return self._campo2
  
  #set
  @temperatura.setter
  def temperatura(self, novo_valor):
    if novo_valor < -273.15:
      raise ValueError("Erro: Temperatura abaixo de (-273.15)!")
    print(f"Nova Temperatura = {novo_valor}")
    self._temperatura = novo_valor
  
  @campo2.setter
  def campo2(self, novo_valor):
    self._campo2 = novo_valor