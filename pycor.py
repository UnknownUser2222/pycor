print("Requires Python 3.10.0 or later.")
print("Welcome to the PyCor v1.01.0")
print("Type help_pycor for help.")
x = ""
while x != "0":
    x = input(">> ")

    cmd1 = "PyCor Objects: In device's memory. Will reset when restarted"
    if x == str("help_pycor"):
        print("add_object - Adds a object to the list")
        print("list_objects - Shows the list of objects")
        print("add_key - Adds a key to the registry")
        print("add_python_key - Adds a Python variable if an 'object' does not work")
        print("add_script - Adds a Python script")
        print("remove_object - Removes an object.")
        print("remove_python_key - Deletes a Python key.")
    elif x == str("add_script"):
        input("Function name: ")
        input("Function code: {__one_line_script: ")
        print("Script saved successfully")
    elif x == str("remove_object"):
        input("Name: ")
        print("Successfully removed object")
    elif x == str("add_python_key"):
        print("Python keys can be useful if an 'object' does not work.")
        input("Name: ")
        input("Value: ")
        print("Successfully added Python key")
    elif x == str("remove_python_key"):
        input("Name: ")
        print("Successfully deleted")
    elif x == str("list_objects"):
        print(cmd1)
    elif x == str("add_key"):
        input1 = input("WARNING: Adding keys without a reason might require a reinstall. Are you sure do you want to continue? ([Y]es or [N]o)")
        if input1 == "Y":
           key_name =  input("Key name: ")
           key_type = input("Key type: ")
           key_value = input("Key value: ")
           print("Key " + key_name + " with type " + key_type + " as " + key_value + " successfully added to registry")
    elif x == str("add_object"):

        cmd2_1 = input("Name: ")
        cmd2_2 = input("Value: ")
        print("Successfully added to dictionary")
        print(cmd1)
    elif x == str(""):
     False
    else:
        print("This term is not a command or a script. Please check if you have any typos in the scripts you typed.")


