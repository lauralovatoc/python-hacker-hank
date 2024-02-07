def mutate_string(string, position, character):
    lista = list(string)
    lista[position] = character

    result = ''.join(lista)
    return result


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)