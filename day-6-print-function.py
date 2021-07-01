# TASK:
# The included code stub will read an integer, , from STDIN.
# Without using any string methods, try to print the following:
# 123...n
# Note that "" represents the consecutive values in between.

if __name__ == '__main__':
    n = int(input("Enter a number between 1 and 125"))
    for i in range(1, n+1):
        print(i, end='')

# range(start, stop[, step]) -> range object return an object that
# produces a sequence of integers from start (inclusive) to
# stop (exclusive) by step.
# start defaults to 0, and step defaults to 1.
