##não terminei

def minion_game(string):
    result_kevin = 0
    result_stuart = 0
    tam = len(string)

    for i in range (0, tam):
        #Kevin
        if string[i] == 'A' or string[i] == 'E' or string[i] == 'I' or string[i] == 'O' or string[i] == 'U':
            result_kevin += 1

            for j in range (i+1, tam):
                    result_kevin += 1

        #Stuart
        else:
            result_stuart += 1

            for j in range(i+1, tam):
                    result_stuart += 1

    if result_kevin > result_stuart:
        print("Kevin",result_kevin)
    elif result_kevin < result_stuart:
        print("Stuart",result_stuart)
    elif result_kevin == result_stuart:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
