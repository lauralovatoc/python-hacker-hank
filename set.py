def average(array):
    sets = set(array)
    soma = sum(sets)
    num = len(sets)

    return soma / num


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)