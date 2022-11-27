# 19.2.4  Counting Words With a Given Prefix
# You are given a list of string words and a string pref.
# Return the number of strings in words that contain pref as a prefix.
# A prefix of a string s is any leading contiguous substring of s.

def prefix_count(words: list[str], pref: str) -> int:
    word_count = 0
    for items in words:
        if items[:2] == pref:
            word_count += 1
    return word_count


words = ["pay","attention","practice","attend"]
pref = "at"
print(prefix_count(words, pref))
words = ["coopedu","win","loops","success"]
pref = "code"
print(prefix_count(words, pref))

