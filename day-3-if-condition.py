if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 1:
        print('Weird')
    elif 2 <= n <= 5:
        print('Not Weird')
    elif 6 <= n <= 20:
        print('Weird')
    else:
        print('Not Weird')
       

# Frequently, a program needs to skip over some statements, execute a 
# series of statements repetitively, or choose between alternate sets
# of statements to execute.
# That is where control structures come in. A control structure directs
# the order of execution of the statements in a program (referred to as
# the program’s control flow).
# In a Python program, the if statement is how we perform this sort of 
# decision-making. It allows for conditional execution of a statement or
# group of statements based on the value of an expression. Syntax:
# if <expr>:   #<expr> is an expression evaluated in boolean
#     <statements>   #these are valid Python statements, which must be indented. 

# Sometimes, you want to evaluate a condition and take one path if it 
# is true but specify an alternative path if it is not. This is accomplished
# with an else
# clause:
# if <expr>:
#     <statement(s)>
# else:
#     <statement(s)>
# If <expr> is true, the first suite is executed, and the second is skipped.
# If <expr> is false, the first suite is skipped and the second is executed.

# There is also syntax for branching execution based on several alternatives. 
# For this, use one or more elif (short for else if) clauses. Python evaluates 
# each <expr> in turn and executes the suite corresponding to the first that is
# true. If none of the expressions
# are true, and an else clause is specified, then its suite is executed:

# if <expr>:
#     <statement(s)>
# elif <expr>:
#     <statement(s)>
# elif <expr>:
#     <statement(s)>
#     ...
# else:
#     <statement(s)>
# At most, one of the code blocks specified will be executed. If an else clause
# isn’t included, and all the conditions are false, then none of the blocks will
# be executed.
