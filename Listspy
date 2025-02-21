if __name__ == '__main__':
    N = int(input())

    lista = []

    for i in range(N):
        linha = input()

        comando = linha.split(" ")[0]

        if comando == "insert":
            posicao = int(linha.split(" ")[1])
            num = int(linha.split(" ")[2])
            lista.insert(posicao, num)
            #função insert --> (posição, caractere inserido)

        if comando == "remove":
            num = int(linha.split(" ")[1])
            lista.remove(num)
            #função remove --> remove um elemento da lista

        if comando == "append":
            num = int(linha.split(" ")[1])
            lista.append(num)
            #função append --> adiciona um elemento ao final da lista

        if comando == "print":
            print(lista)

        if comando == "sort":
            lista.sort()
            #função sort --> organizar (reverse, key)
            #reverse = True (ordem decrescente), reverse = False ( ordem crescente), default False
            #key --> se a lista tiver duas colunas [0][1], vc coloca o numero que deve ser padrão para organizar

        if comando == "reverse":
            lista.reverse()
            #função reverse - reverte a ordem dos elementos

        if comando == "pop":
            lista.pop()
            #função pop --> retira o ultimo item (pega ele), (posição do numero a ser removido)
            #default [-1] = ultimo numero
