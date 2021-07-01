print("Hello", "World!")
print("This is Roshan")

# Running this code will print:
# Hello World!
# This is Roshan

# Lets see the signature of our print().
# print(*objects, sep= ' ', end='\n', file=sys.stdout, flush=False)")
# We see many other parameters here, but we passed only one in above
# code: *objects = "Hello", "World".

# If we see a little more closely, we'll see that in most of the parameters
# the default arguments are provided using '='. Lets see them one by one
# sep= ' ' => this is the separator if multiple arguments are passed
# using a comma. This separator tells python to provide a space (' ') in
# between the 'objects'. We can see this in our code as well- this
# told python to include a space between 'Hello' and 'World!'
# end='\n' => this tells python what to do after the print statement is
# executed. The '\n' is the newline character which inserts a new line
# in the program. That's why in the output we see 'This is Roshan'
# getting printed in the next line.
# Similarly file=sys.stdout and flush=False) too have the default
# argument values.

# So here we only passed the one argument (*objects'). We could have
# skipped that as well, but then Python would have only printed the '\n'.
