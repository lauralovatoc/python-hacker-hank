import textwrap

def wrap(string, max_width):
    result = []
    string.strip()
    
    for i in range(0,len(string),max_width):
        result.append(string[i:i+max_width])
    
    x = "\n".join(result)
        
    return x
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
