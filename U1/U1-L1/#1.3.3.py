# 1.3.3 开发一个简单的欢迎程序，新生输入自己的姓名和年级后，控制台会显示 “欢迎 xxx 开始 xx 年级的学习”
name = input("请输入姓名：")
grade = input("请输入年级：")
print("欢迎 %s 开始 %s 年级的学习！" % (name, grade))
