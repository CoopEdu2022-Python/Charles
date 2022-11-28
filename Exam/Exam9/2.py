# 2.2  Capitalize the Title
# You are given a string title consisting of one or more words separated by a single space,
# where each word consists of English letters.
# Capitalize the string by changing the capitalization of each word such that:
# - If the length of the word is 1 or 2 letters, change all letters to lowercase.
# - Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
# Return the capitalized title.
def capitalize_title(title: str) -> str:
    title_list = title.lower().split(" ")
    for i, items in enumerate(title_list):
        if len(items) > 2:
            title_list[i] = items.capitalize()
    new_title = ""
    for items in title_list:
        new_title += (items + " ")
    return new_title


print(capitalize_title("capiTalIze tHe lEtTeR OF titLe"))

