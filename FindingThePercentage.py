if __name__ == '__main__':
    n = int(input())#numero de estudantes
    student_marks = {} #dicionario {"nome":"[lista de scores]"}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()#nome do estudante escolhido

    grades = []
    student_name =[]
    
    lists = list(student_marks.items())
    
    for i in range(n):
        student_name.append(lists[i][0])
        grades.append(lists[i][1])
    
    mean = []

    for i in range(n):
        mean.append(sum(grades[i])/len(scores))
    
    for i in range(n):
        if student_name[i] == query_name:
            result = "{:.2f}".format(mean[i])
            print(result)
