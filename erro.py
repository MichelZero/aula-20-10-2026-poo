# autor: Michel
# data: 20/10/2026

# erro
valor = 10
print(valor)
valor = float(valor)
print(valor)
# valor = input("informe um valor: ")
# valor = int(valor)
# print(valor)
# valor = float(valor)
# print(valor)


# try / except
try:
  valor = input("informe um valor: ")
  valor = int(valor)
  print(valor)
  valor = float(valor)
  print(valor)
except ValueError as e:
  print(f"Erro ao converter para int {e}!")
  
input()
  