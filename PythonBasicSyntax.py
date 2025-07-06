if 10 > 5:
    print("This is true!")
    print("I am tab indentation")


print("I have no indentation")

a = 10
print(type(a))

b = 'GeeksforGeeks'
print(type(b))

# comments start with

'''
Multi Line comment.
Code will print name.
but this is a string
'''

sentence = "This is a very long sentence that we want to " \
           "split over multiple lines for better readability."

print(sentence)


# Line continuation within square brackets '[]'
numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]

print(numbers)


# Taking input from the user
name = input("Please enter your name: ")

# Print the input
print(f"Hello," + name)