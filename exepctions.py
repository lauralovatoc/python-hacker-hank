if __name__ == '__main__':

    t = int(input())

    for i in range(t):
        x = str(input())
        a = x.split()[0]
        b = x.split()[1]

        if b.isalnum() == False:
            print(f"Error Code: invalid literal for int() with base 10: '{b}'")
        elif a.isalnum() == False:
            print(f"Error Code: invalid literal for int() with base 10: '{a}'")
        elif int(b) == 0:
            print("Error Code: integer division or modulo by zero")
        else:
            result = int(a)//int(b)
            print(result)