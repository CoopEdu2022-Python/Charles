# 3.2.11 for循环：制作一个动态的进度条（提示：使用 print 函数的 end 参数）
import time
for i in range(8):
    a = "*"
    print(a * i, end="")
    time.sleep(0.5)
