# TASK:
# The provided code stub reads two integers, a and b, from STDIN.
# Add logic to print two lines. The first line should contain the
# result of integer division, a//b . The second line should 
# contain the result of float division, a/b .

a = int(input())
b = int(input())

print("Integer division =", a//b)
print("Float division =", a/b)

# Integer division or Floor division : The // operator first divides
# the number on the left by the number on the right and then rounds down
# to an integer. The round-off is done by truncating/ignoring the value
# after the decimal point.
# Float division: division with the / operator always returns a float.
