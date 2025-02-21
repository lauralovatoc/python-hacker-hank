if __name__ == '__main__':
    mylist = []
    scn_lowest = []
    new_list = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        mylist.append([name, score])

    values = sorted(mylist, key=lambda x: x[1], reverse=True)
    lowest_value = values[-1][1]

    for i in range(len(values)):
        if values[i][1] != float(lowest_value):
            new_list.append(values[i])

    scn_lowest_value = new_list[-1][1]

    for i in range(len(new_list)):
        if new_list[i][1] == scn_lowest_value:
            scn_lowest.append(new_list[i][0])

    scn_lowest.sort()
    for x in scn_lowest:
        print(x)

