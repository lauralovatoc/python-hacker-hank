if __name__ == '__main__':
    def lerNotas():
        nota = float(input("Informe a nota: "))
        return nota


    def resultado(a,b):
        return (a+b)/2


    nota1 = lerNotas()
    nota2 = lerNotas()

    media = resultado(nota1,nota2)
    print("Média do aluno(a):",media)

    if media >= 7.00:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")