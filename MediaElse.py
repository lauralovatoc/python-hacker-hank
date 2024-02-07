if __name__ == '__main__':
    A = float(input("Valor de A: "))
    B = float(input("Valor de B: "))

    media_final = (A+B)/2

    if media_final >= 7.00:
        print("A média: %.1f - APROVADO"% media_final)
    else:
        print("A média %.1f - REPROVADO"% media_final)

    #elif = else if