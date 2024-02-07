#receber uma string e deixar a primeira letra de cada palavra em letra maisucula --> funcoes capitalize() e split()
if __name__ == '__main__':
    s = input()
    result = " ".join(i.capitalize() for i in s.split(" "))
    print(result)
