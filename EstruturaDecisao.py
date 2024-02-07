if __name__ == '__main__':
    A = input("Digite um valor para a variável A: ")
    B = input("Digite um valor para a variável B: ")

    if(A > B):
        aux=A
        A=B
        B=aux

    print("Valor da variável A:",A)
    print("Valor da variável B:",B)