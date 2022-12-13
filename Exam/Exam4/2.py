def verdict_password():
    while True:
        password = input("Enter your password: ")
        if password == "q":
            return False
        elif len(password) < 8 or (not password.isalnum()):
            if len(password) < 8:
                print("There must be more than 8 characters in your password.")
            if not password.isalnum():
                print("Wrong password format, you can only enter numbers and alphabets.")
        else:
            return password


def reset_password(login_info):
    while True:  # 用户名判断
        username = input("Please enter your Student name:")
        if username == "q":
            return False
        if username in login_info.keys():
            break
        else:
            print("Wrong username, please enter again.")
    password = verdict_password()  # 密码正确输入判断
    if password == 0:
        return False
    print("You can reset your password now.")
    password = int(input("Enter your password: "))
    for i in range(0, len(login_info[username])):
        if password == login_info[username][i]:
            print("Please set a password you've never used before")
            password = verdict_password()  # 密码正确设置判断
            if password == 0:
                return False
        if password not in login_info[username]:
            login_info[username] = login_info[username].insert(0, password)
            if len(login_info[username]) >= 3:  # 多于3个就删除
                login_info[username].pop()
            print("Password has been reset")
            return tuple([username, password])


info = {"user1": ["12345678"], "user2": ["12345678", "23456789", "34567890"]}
print(reset_password(info))

