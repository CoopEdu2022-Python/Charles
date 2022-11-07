def is_palindrome(s):
    s_ = ""
    for item in s:
        if item.isalnum():
            s_ += item.lower()
    return s_ == s_[::-1]


print(is_palindrome(" "))
