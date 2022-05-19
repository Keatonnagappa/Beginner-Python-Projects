### A Lambda Function in Python programming is an anonymous function or a function having no name. It is a small and restricted function having no more than one line. Just like a normal function, a Lambda function can have multiple arguments with one expression. ###

# Traditional function.


def check_even(num):
    return num % 2 == 0


mynum = [1, 2, 3, 4, 5, 6]

# iterating through our mynum variable. (we can also list these items instead of iterating through them)

for item in map(check_even, mynum):
    print(item)


# Conveting above function to a listed Lambda Expression

map_variable = list(map(lambda num: num % 2 == 0, mynum))

print(map_variable)


# Traditional use of the filter function. (we can also list these items instead of iterating through them)

for item in filter(check_even, mynum):
    print(item)

# Converting the above filter function into a listed Lambda expression 

filter_variable = list(filter(lambda num: num % 2 == 0, mynum))

print(filter_variable)
