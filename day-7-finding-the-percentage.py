if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    # print(student_marks[query_name])
    average = sum(student_marks[query_name])/ float(len(student_marks[query_name]))
    print("{:.2f}".format(average))
