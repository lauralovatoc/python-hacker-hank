# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    countries = []
    
    for _ in range(n):
        countries.append(str(input()))
    
    result = len(set(countries))
    print(result)
