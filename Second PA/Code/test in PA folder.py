def enter_system(id_number: str, password: str):
    with open("../account & password", "r") as f:
        a = f.readlines()
        a.pop(0)
        for i, items in enumerate(a):
            a[i] = items.rstrip("\n")[-16:]
        v_password = ""
        for items in a:
            print(items[:5])
            print(items[8:])
            print(items[:5] == id_number)
            if items[:5] == id_number:
                v_password = items[8:]
                break
        if password == v_password:
            return "access granted"
        else:
            return "access denied(you can try again if you want hhhh)"


print(enter_system("s_333", "12345678"))