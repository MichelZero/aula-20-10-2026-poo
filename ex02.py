# autor: Michel
# data: 20/10/2026

class Jogador:
    # parte 1: O construtor da classe
    def __init__(self, nome, pontuacao=0):
        self.nome = nome          # Passa pelo setter
        self.pontuacao = pontuacao

    # parte 2: O GETTER: Permite ler o atributo como se fosse uma variável normal
    @property
    def nome(self):
        return self._nome

    # parte 3: O SETTER: Intercepta a atribuição (ex: jogador.nome = X) para validar e formatar
    @nome.setter
    def nome(self, novo_nome):
        # Remove espaços extras das pontas
        novo_nome_limpo = novo_nome.strip()
        
        if not novo_nome_limpo:
            raise ValueError("O nome do jogador não pode estar vazio!")
            
        print(f"-> Nome atualizado para: '{novo_nome_limpo}'")
        self._nome = novo_nome_limpo


# --- TESTANDO O CÓDIGO ---
p1 = Jogador("  Carlos Silva   ")  # O setter limpa os espaços automaticamente

print(p1.nome)  # Exibe: 'Carlos Silva'

# Alterando o nome depois:
p1.nome = "   Ana Souza  "  # O setter intercepta, limpa e valida
print(p1.nome)  # Exibe: 'Ana Souza'

# Tentando colocar um nome vazio:
try:
    p1.nome = "   "
except ValueError as e:
    print(e)