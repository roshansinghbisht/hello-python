if __name__ == '__main__':
    n = int(input("Enter a number between 1 and 20"))

    for i in range(n):
        print(i**2)
        
# A module is a file containing Python definitions and statements.
# The file name is the module name with ‘.py’ appended.

# Many programming languages have a special function that is 
# automatically executed when an operating system starts to run a 
# program. This function is usually called main(). On the other hand,
# the Python interpreter executes scripts starting at the top of the
# file, and there is no specific function that Python automatically 
# executes.
# Nevertheless, having a defined starting point for the execution of a 
# program is useful for understanding how a program works.

# Say if we wanted to execute some lines of code only when we run the 
# script directly, and not when the file is imported in other modules?
# Whenever we run a script, python actually sets a special built-in
# variable called ‘__name__’ for any module. Python recognises the
# module as the main program(the script which runs), and sets the
# __name__ variable for that module as __main__. For any modules which 
# are imported in the script, this built-in __name__ variable is just
# set to the name of that module.

# Hence in above code, the if statement just checks whether we are 
# running the script directly or not:
# If __name__ = main is True, this means that we're running the 
# script directly. Else, we are running it after importing it elsewhere.

# Python For loop syntax:
# for i in <collection>
#        <loop body>
    
# range(<end>) function in Python returns an iterable that yields integers 
# starting with 0, up to but not including <end>
# Example: range(4) will return 0,1,2,3.
# --Iterables are objects that can return one of their elements at a time.
