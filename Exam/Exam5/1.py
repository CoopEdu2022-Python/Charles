def iterate_password(user_info):
    while 1:
        original_password = input("Enter your original password: ")
        if original_password != user_info["password"]:
            continue
        else:
            while 1:
                new_password0 = input("Enter your new password: ")
                new_password1 = input("Confirm your new password: ")
                digit = 0
                alphabet = 0
                upper_alphabet = 0
                for i in new_password0:
                    if i.isdigit():
                        digit = 1
                        continue
                    if i.islower():
                        alphabet = 1
                        continue
                    if i.isupper():
                        upper_alphabet = 1
                if new_password1 != new_password0:
                    print("The two new passwords are different.")
                if (digit == 0 and alphabet == 0) or (digit == 0 and upper_alphabet == 0) or (alphabet == 0 and upper_alphabet == 0):
                    print("The password needs to use both letters and numbers.")
                    continue
                if len(new_password0) < 8:
                    print("The password needs to have at least 8 items.")
                    continue
                user_info["password"] = new_password1
                print("New password has been set.")
                return True


user_info = {"username": "user_1", "password": "a1234567A"}
print(iterate_password(user_info))
