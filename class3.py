# Listas que almacenarán los países y la problacion
paises = ['Argentina', 'Bolivia', 'Perú', 'Brasil', 'Ecuador']
problacion = [45000000, 11000000, 33000000, 213000000, 17000000]

# Ordena alfabéticamente utilizando el método de ordenamiento 'bubble sort'
n = len(paises)
for i in range(n-1):
    for j in range(0, n-i-1):
        if paises[j] > paises[j+1]:
            paises[j], paises[j+1] = paises[j+1], paises[j]
            problacion[j], problacion[j+1] = problacion[j+1], problacion[j]

# imprimir los países ordenados alfabéticamente
print("\nPaíses y problacion ordenados alfabéticamente:")
for pais, poblacion in zip(paises, problacion):
    print(f"{pais}: {poblacion} problacion")


# Ordenar por la cantidad de problacion del país de mayor a menor utilizando bubble sort 
for i in range(n-1):
    for j in range(0, n-i-1):
        if problacion[j] < problacion[j+1]:
            problacion[j], problacion[j+1] = problacion[j+1], problacion[j]
            paises[j], paises[j+1] = paises[j+1], paises[j]


# Imprimir los resultados por cantidad de problacion de mayor a menor
print("\nPaíses y problacion ordenados por cantidad de problacion (de mayor a menor):")
for pais, poblacion in zip(paises, problacion):
    print(f"{pais}: {poblacion} problacion")