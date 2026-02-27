from utils import maior_e_menor, calcular_media


def obter_numeros():
    entrada = input("Digite números separados por espaço: ")

    try:
        numeros = [float(num) for num in entrada.split()]
        return numeros
    except ValueError:
        print("⚠️ Você digitou algo inválido.")
        return None


def main():
    print("=" * 40)
    print("📊 ANALISADOR DE NÚMEROS")
    print("=" * 40)

    while True:
        numeros = obter_numeros()

        if numeros:
            maior, menor = maior_e_menor(numeros)
            media = calcular_media(numeros)

            print("\n📈 Resultado:")
            print(f"Maior número: {maior}")
            print(f"Menor número: {menor}")
            print(f"Média: {media:.2f}")
            print(f"Quantidade: {len(numeros)}")

        repetir = input("\nDeseja analisar outra lista? (s/n): ").lower()
        if repetir != "s":
            print("Encerrando programa...")
            break


if __name__ == "__main__":
    main()