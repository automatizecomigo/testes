import re
import requests

# URL do site para raspar
url = 'https://www.mcce.org.br/newsletter'

# Fazendo a requisição HTTP
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Encontrando todos os endereços de e-mail no conteúdo da página usando regex
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', response.text)

    # Adicionando aspas simples em torno de cada endereço de e-mail e formatando em colunas
    max_len = max(len(email) for email in emails) + 2  # Comprimento máximo de e-mail
    formatted_emails = [f"'{email}',{' ' * (max_len - len(email))}" for email in emails]

    for email in formatted_emails:
        print(email)
else:
    print('Falha ao obter a página:', response.status_code)
