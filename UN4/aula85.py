lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y))

lista = [
    (x,y,z)
    for x in range(3)
    for y in range(3)
    for z in range(3)

]

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

lista1 = [
    letra 
    for letra in 'Luis'
]
print(lista)
print(lista1)