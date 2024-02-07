if __name__ == '__main__':
    s = input()
    result = " ".join(i.capitalize() for i in s.split(" "))
    print(result)