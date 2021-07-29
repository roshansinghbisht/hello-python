def string_operations(text):
    print(text)
    print(text.capitalize())
    print(text.casefold())
    print(text.encode())
    print(text.isalpha())
    print(text.swapcase())
    print(text.title())
    print(text.format("This is going to replace the braces"))


if __name__ == '__main__':
    input_string = input("Enter any string")
    string_operations(input_string + " {}")
