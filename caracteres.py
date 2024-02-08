if __name__ == '__main__':
    s = input()

    for i in range(0, len(s)):
        if s[i].isalnum():
            print(True)
            break
        elif i ==len(s)-1 and s[i].isalnum() == False:
            print(False)

    for i in range(0, len(s)):
        if s[i].isalpha():
            print(True)
            break
        elif i==len(s)-1 and s[i].isalpha() == False:
            print(False)

    for i in range(0, len(s)):
        if s[i].isdigit():
            print(True)
            break
        elif i==len(s)-1 and s[i].isdigit() == False:
            print(False)

    for i in range(0, len(s)):
        if s[i].islower():
            print(True)
            break
        elif i==len(s)-1 and s[i].islower() == False:
            print(False)

    for i in range(0, len(s)):
        if s[i].isupper():
            print(True)
            break
        elif i==len(s)-1 and s[i].isupper() == False:
            print(False)