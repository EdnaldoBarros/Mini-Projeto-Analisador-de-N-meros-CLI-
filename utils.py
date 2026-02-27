def maior_e_menor(lista):
    if not lista:
        raise ValueError("A lista não pode estar vazia.")

    maior = menor = lista[0]

    for numero in lista:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

    return maior, menor


def calcular_media(lista):
    return sum(lista) / len(lista)