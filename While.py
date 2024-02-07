if __name__ == '__main__':
    qntd = 0
    soma = 0
    media = 0

    valor = float(input("Digite um valor: "))

    while valor > 0.0:
        soma += valor
        qntd+=1

        valor = float(input("Digite um valor: "))

    media = soma/qntd
    print("Soma total:",soma)
    print("Quantia de valores digitados",qntd)
    print("Média Final:",media)