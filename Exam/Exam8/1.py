def check_if_pangram(sentence: str) -> bool:
    alphabet = "qwertyuiopasdfghjklzxcvbnm"
    for letter in alphabet:
        if sentence.find(letter) == -1:
            return False

    return "sentence contains at least one of every letter"


print(check_if_pangram("CoopEdu"))
