if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    average = sum(student_marks[query_name])/ float(len(student_marks[query_name]))
    print("{:.2f}".format(average))
    
# Passing an integer after the ':' will cause that field to be a minimum
# number of characters wide.

# format(): Perform a string formatting operation. The string on which 
# this method is called can contain literal text or replacement fields 
# delimited by braces {}. Each replacement field contains either the 
# numeric index of a positional argument, or the name of a keyword 
# argument. Returns a copy of the string where each replacement field is 
# replaced with the string value of the corresponding argument.
