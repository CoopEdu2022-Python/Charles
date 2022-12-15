# 1.3.4 使用 input() 输入你的姓名、性别、学号，按照下方格式打印所有信息（左右对齐即可）
name = str(input("Enter a name: "))
gender = str(input("Enter your gender: "))
ID = int(input("Enter your format ID: "))
print("---- info ----")
print("Name:  %s" % name, "Gender:   %s" % gender, "ID:   %d" % ID, sep='\n')
print("--------------")
