# 3.1.11 制作一个动态的进度条（提示：使用 print 函数的 end 参数）
import time
i = 0
while i <= 5:
    a = "*" * 4
    i += 1
    time.sleep(0.5)
    print(a, end="")


print("\n", "加载完毕")
