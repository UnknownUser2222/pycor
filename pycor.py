print("Welcome to PyCor v1.04.0 // 1012")
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
        print("list_version - Shows all the versions of the program installed")
        print("change_program_cmds - Changes the commands of the program (except current built-in commands)")
        print("change_pcr_regedit - Changes the registry values for a PCR file")
        print("update_pcr - Updates the current PCR file")
        print("repair_pcr - Repairs the current PCR file")
        print("add_iso - Mounts a ISO file")
        print("create_fsc - Creates a FSC file")
        print("lts_edit - Edits a LTS module selected.")
        print("exp_change - Changes the EXP module")
        print("refresh_pycor - Passes a refresh")
        print("exit - Exits the program")
        print("exit_bst - Exits the BST")
        print("exit_client - Exits the client")
        print("PyCorMgr - Runs PyCorMgr.pcr")
        print("NOTE: New commands are now shown in PyCorMgr.pcr")
    elif x == str("PyCorMgr"):
        print("----------------------------------------------------------------------------------------")
        print("|                            PyCor Manager v1.0.1                                      |")
        print("|                            Select a item to run                                      |")
        print("|  [1] Exit   [2] Add file    [3] Add ISO   [4] Add root file  [5] Add package         |")
        print("|  [6] Add shell root [7] Add config [8] Add PYW file                                  |")
        print("|______________________________________________________________________________________|")
        while x != "0":
            x = input("""app@pycor: ~su: github.com/UnknownUser2222/pycor 
 $ """)
            if x == "1":
                print("Exiting...")
                exit("""EXIT: At package line 3, exit confirmed by PyCorMgr.pcr, Codename is x-success
Trace module became <eof> interrupted by exit key.
PYCOR_MGR_0""")
                exit(-193847291)
            if x == "2":
                input("Name: ")
                input("Directory: ")
            if x == "3":
                input("Name: ")
                input("Directory: ")
            if x == "4":
                input("Name: ")
                input("Directory: ")
            if x == "5":
                input("Name: ")
                input("Directory: ")
            if x == "6":
                input("Name: ")
                input("Directory: ")
            if x == "7":
                input("Name: ")
                input("Directory: ")
            if x == "8":
                input("Name: ")
                input("Directory: ")
    elif x == str("exit_client"):
        exit(0)
    elif x == str("exit_bst"):
        exit(1)
    elif x == str("exit"):
        exit(0)
    elif x == str("refresh_pycor"):
        print("Refreshed program.")
    elif x == str("exp_change"):
        input("Name: ")
        print("Successfully changed module.")
    elif x == str("lts_edit"):
        input("Value: ")
        print("Successfully changed values.")
    elif x == str("create_fsc"):
        input("Name: ")
        print("Successfully created FSC file.")
    elif x == str("change_pcr_regedit"):
        input("Directory: ")
        print("Successfully mounted ISO file.")
    elif x == str("repair_pcr"):
        print("Checking for errors...")
        print("Repairing...")
        print("Successfully repaired.")
    elif x == str("update_pcr"):
        print("Checking for updates")
        print("Successfully updated current file")
    elif x == str("change_pcr_regedit"):
        input("Name: ")
        input("Value: ")
        print("Successfully changed values")
    elif x == str("update_pcr"):
        print("Version: 1.02.0 Build 1003")
    elif x == str("change_program_cmds"):
        file_name = input("Name of extension/PCR file: ")
        directory = input("Directory: ")
        print("Enabling " + file_name + "'s features...")
        print("Disabling current commands (except PyCor commands)...")
        print("Checking version of file...")
        print("Enabling commands...")
        print("Successfully switched program mode")
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
        input1 = input(
            "WARNING: Adding keys without a reason might require a reinstall. Are you sure do you want to continue? ([Y]es or [N]o)")
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
