cube = lambda x: x ** 3
def fibonacci(n):
    # return a list of fibonacci numbers
    resultList = []

    for i in range(0, n):
        if i == 0 or i == 1:
            resultList.append(i)
        elif i >= 2:
            new_number = resultList[i - 1] + resultList[i - 2]
            resultList.append(new_number)
    return resultList


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))