digital_key = input("Digital key: ")
if digital_key == "01032022":
    print("""
    PyCor Manager (Owner)
    Select a key to confirm
    [1] View authorised applications
    """)
    x = ""
    while x != "0":
        x = input("NET SUDO CMD: ")
        if x == "1":
            print("""
            Authorised applications:
            1: GitHub OEM: 2635134
            2: VSCODE OEM: 8485839
            """)
