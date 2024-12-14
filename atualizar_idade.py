import re
from datetime import datetime

# Função para calcular a idade
def calcular_idade(data_nascimento):
    hoje = datetime.today()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

# Data de nascimento do usuário
data_nascimento = datetime(2005, 10, 23)

# Calculando a idade atual
idade_atual = calcular_idade(data_nascimento)

# Função para substituir a idade no README
def atualizar_arquivo(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    
    # Expressão regular para encontrar o padrão "I'm+<qualquer_numero>+years+old"
    novo_conteudo = re.sub(r"I'm\+(\d+)\+years\+old", f"I'm+{idade_atual}+years+old", conteudo)
    
    # Salvando o conteúdo atualizado de volta no arquivo
    with open(arquivo, 'w', encoding='utf-8') as f:
        f.write(novo_conteudo)

# Chame a função para atualizar o README
atualizar_arquivo('README.md')
