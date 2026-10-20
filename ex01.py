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




# --- TESTANDO O CÓDIGO ---
# criando o objeto Termometro com temperatura inicial de 30°C
meu_termometro = Termometro(30)  # Funciona (chama o setter)

print(meu_termometro.temperatura)  # Lê usando o getter -> Saída: 30.0

# Tentando colocar uma temperatura válida:
meu_termometro.temperatura = 30.5  # Funciona perfeitamente

# Tentando colocar uma temperatura inválida:
try:
    meu_termometro.temperatura = -300  # Dispara a exceção do setter
except ValueError as e:
    print(e)