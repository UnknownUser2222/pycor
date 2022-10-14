print("Requires Python 3.10.0 or later.")
print("Welcome to the PyCor v1.00.0")
print("Type help_pycor for help.")
x = ""
while x != "0":
    x = input(">> ")

    cmd1 = "PyCor Objects: In device's memory. Will reset when restarted"
    if x == str("help_pycor"):
        print("add_object - Adds a object to the list")
        print("list_objects - Shows the list of objects")
    elif x == str("list_objects"):
        print(cmd1)
    elif x == str("add_object"):

        cmd2_1 = input("Name: ")
        cmd2_2 = input("Value: ")
        print("Successfully added to dictionary")
        cmd1.replace(str(cmd2_1), "PyCor Objects: null")
        print(cmd1)
    elif x == str(""):
     False
    else:
        print("This term is not a command, script, object or file.")


