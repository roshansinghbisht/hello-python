def factorial_using_while_loop(number):
    current = 1
    product = 1
    while current <= number:
        product *= current
        current += 1
    return product


def factorial_using_for_loop(number):
    product = 1
    for i in range(1, number+1):
        product *= i
    return product


input_number = int(input("Enter a number"))
print(factorial_using_while_loop(input_number))
print(factorial_using_for_loop(input_number))
