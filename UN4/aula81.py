# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)
# sorted(lista)

from rich.console import Console
from rich.table import Table

lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# Ordena a lista pelo nome
lista.sort(key=lambda item: item['nome'])

# Cria o console
console = Console()

# Cria a tabela
tabela = Table(
    title="Lista de Pessoas",
    title_style="bold cyan",
    header_style="bold magenta",
    border_style="blue"
)

# Adiciona as colunas
tabela.add_column("Nº", justify="center", style="yellow")
tabela.add_column("Nome", style="green")
tabela.add_column("Sobrenome", style="white")

# Adiciona os dados
for numero, item in enumerate(lista, start=1):
    tabela.add_row(
        str(numero),
        item['nome'],
        item['sobrenome']
    )

# Exibe a tabela
console.print(tabela)