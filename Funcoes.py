def numeros_pares(lista):
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    return pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = numeros_pares(numeros)

print("Números pares:", pares)
