import csv
from collections import Counter

direc = ""
arch_juegos_de_mesa = open(direc + "bgg_db_1806.csv", "r", encoding='utf-8')
reader = csv.reader(arch_juegos_de_mesa, delimiter = ",")

next(reader)
lista_nombres = []
juegos = {}

for lista in reader:
    if (int(lista[4]) < 3 and lista[17] == "Card Game"):
        lista_nombres.append(lista[3])
    juegos[lista[13]] = int(lista[12])

print(lista_nombres)

max = dict(Counter(juegos).most_common(10))
print('Los 10 links de fotos de los juegos con mas votos: ')
print(max.keys())
arch_juegos_de_mesa.close()