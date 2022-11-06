def reverse_vowels(s: str) -> str:
    vowels = "aeiou"
    new_str = ""
    record_list = []
    for char in s:
        temp_char = char
        if char.lower() in vowels:
            record_list.insert(0, char)
            new_str += ","
        else:
            new_str += temp_char
    i = 0

    while new_str.find(",") != -1:
        new_str = new_str.replace(",", record_list[i], 1)
        i += 1
    return new_str


print(reverse_vowels("CoopEdu2022"))
