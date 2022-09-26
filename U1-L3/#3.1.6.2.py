import random
a = 0
for i in range(1, 31):
    score = random.randint(-1, 101)#int(input("Enter the score"))
    a += score
    if score < 0 or score > 100:
        print("Error score, enter again")
        continue
print("The average score for these 30 students is:", a/30)
