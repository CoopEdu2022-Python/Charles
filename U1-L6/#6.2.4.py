dict_rome = {"I": 1,
             "V": 5,
             "X": 10,
             "L": 50,
             "C": 100,
             "D": 500,
             "M": 1000}
dict_special = {"IV": 4,
                "IX": 9,
                "XL": 40,
                "XC": 90,
                "CD": 400,
                "CM": 900}


def rome_transfer(s):
    temp = []
    for key1 in dict_special.keys():
        if key1 in s:
            s = s.replace(key1, "")
            temp.append(dict_special[key1])
    for i, ele in enumerate(s):
        if ele in dict_rome:
            temp.append(dict_rome[ele])
    return sum(temp)


print(rome_transfer("MCMXCIV"))
