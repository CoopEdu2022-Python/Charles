# 5.2.7 系统里面有多个用户，用户的信息目前保存在元祖中(一一对应），完成简单的登录功能
users = ('root', 'user1', 'user2')
passwords = ('123', 'abc', '@*#')
# 提示用户输入用户名和密码
# 如果登录成功，打印欢迎消息
# 如果失败，说明具体的错误原因，让用户重新登陆，共有 3 次机会

b = 0
for i in range(3):
    user_name_input = input("Enter the user name: ")
    password_input = input("Enter the password: ")
    if user_name_input not in users:
        b += 1
        print("User name error, please try again. ")
        print("You got %d chance left." % (2 - i))
    if user_name_input in users:
        j = 0
        a = i
        while j < i:
            if user_name_input == users[j]:
                if password_input != passwords[j]:
                    print("Password error, please try again.")
                    print("You got %d chance left." % (2 - a))
                    if 2 - a == 0:
                        print("Access denied")
                        break
                    a += 1
                    user_name_input = input("Enter the user name: ")
                    password_input = input("Enter the password: ")
                    continue
                if password_input == passwords[j]:
                    print("Access granted")
                    break
            j += 1

        break
    else:
        print("Access granted")
