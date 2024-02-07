if __name__ == '__main__':
    s = input()
    result = " ".join(i.capitalize() for i in s.split(" "))
    print(result)

    #recebe string, transofrma primeira letra de cada palavra em maiuscula, funções: capitalize(), split() e join()