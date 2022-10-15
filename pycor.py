print("Requires Python 3.10.8 or later.")
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
        print("remove_key - Deletes a key")
        print("remove_script - Removes a script.")
        print("add_python_object - Adds a Python object.")
        print("add_pycor_variable - Adds a PyCor variable.")
        print("add_jscript_variable - Adds a JavaScript variable")
        print("remove_python_object - Removes a Python object")
        print("client_redirect_host - Redirects to host server")
        print("connect_to_github_server - Connects to a GitHub repository")
        print("drive_change - Changes the disk drive directory")
        print("More coming soon in v1.02.0!")
    elif x == str("drive_change"):
        drive = input("Drive letter: ")
        print("Changed from this directory to " + drive)
    elif x == str("connect_to_github_server"):
        input("Name of repo: ")
        input("Owner or organization: ")
        print("Successfully joined server.")
    elif x == str("client_redirect_host"):
        input("Name of server: ")
        input("Directory: ")
        print("Successfully joined server.")
    elif x == str("remove_python_object"):
        input("Name: ")
        print("Successfully removed object.")
    elif x == str("add_jscript_variable"):
        input("Name: ")
        input("Value: ")
        print("Successfully added JScript object")
    elif x == str("add_script"):
        input("Function name: ")
        input("Function code: {__one_line_script: ")
        print("Script saved successfully")
    elif x == str("remove_object"):
        input("Name: ")
        print("Successfully removed object")

    elif x == str("remove_script"):
        input("Name: ")
        print("Successfully removed script.")

    elif x == str("add_python_object"):
        input("Name: ")
        input("Value: ")
        print("Successfully added object")

    elif x == str("add_pycor_variable"):
        input("Name: ")
        print("Successfully added variable")
    elif x == str("remove_key"):
        input("Name: ")
        print("Successfully removed key")
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
            key_name = input("Key name: ")
            key_type = input("Key type: ")
            key_value = input("Key value: ")
            print("Key " + key_name + " with type " + key_type + " as " + key_value + " successfully added to registry")
    elif x == str("add_object"):

        cmd2_1 = input("Name: ")
        cmd2_2 = input("Value: ")
        print("Successfully added to dictionary")
        print(cmd1)
    elif x == str(""):
        key = True

    else:
        print("This term is not a command or a script. Please check if you have any typos in the scripts you typed.")


