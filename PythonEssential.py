# Local and Global VariablesIn this task, you'll work with local and global variables to understand their scope.
# Defining a global variable counter with an initial value of 0.

counter = 0

# Creating a function increment_counter() that:Increments the global variable counter by 1.
# Prints the current value of counter.

def increment_counter():
    global counter
    counter += 1
    print(counter)

# Creating another function reset_counter() that:Defines a local variable counter with a value of 0.
# Prints the value of the local counter.

def reset_counter():
    counter = 0
    print(counter)

# Calling the functions increment_counter() three times and then call reset_counter(). Print the global counter after each function call.

increment_counter()
increment_counter()
increment_counter()
reset_counter()
print(counter)


import os

print(os.getcwd())  # Prints the current working directory

print(os.listdir())  # Lists all files and directories in the current working directory

os.mkdir("test_dir")  # Creates a new directory called test_dir

os.chdir("test_dir")  # Changes the working directory to test_dir

print(os.getcwd())  # Prints the new working directory

# Create a new file named test_file.txt inside test_dir.

with open("test_file.txt", "w") as f:
    f.write("This is a test file.")


os.remove("test_file.txt")  # Deletes the test_file.txt file

os.rmdir("test_dir")  # Deletes the test_dir directory



