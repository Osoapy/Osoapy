import datetime
import re

# Defina sua data de nascimento
data_nascimento = datetime.date(2005, 10, 23)  # Exemplo: 14 de maio de 1995

# Calcule a idade atual
hoje = datetime.date.today()
idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

# Caminho para o arquivo README.md
readme_path = 'README.md'

# Abra o arquivo README.md
with open(readme_path, 'r') as file:
    content = file.read()

# Substitua o marcador <!-- AGE --> pela idade calculada
novo_conteudo = re.sub(r'<!-- AGE -->', f'Idade: {idade}', content)

# Salve o conteúdo atualizado no README.md
with open(readme_path, 'w') as file:
    file.write(novo_conteudo)

print(f'Idade atualizada para {idade} no README.md')
