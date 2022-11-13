# 15.1.2  大鱼吃小鱼 [50pts]
# 假设鱼塘的范围为 (x, y)，0 <= x, y <= 10；游戏开始时，在随机位置生成 1 只大鱼和 10 只小鱼
# 大鱼和小鱼随机上下左右移动，每一次移动，大鱼在横竖方向分别最多移动 1 个单位， 小鱼最多移动 1 个单位；当移动到鱼塘边缘时，自动向反方向移动
# 大鱼的体力值为 100，每移动 1 个单位，就消耗 1 点体力；小鱼没有体力值；一次移动结束后，如果大鱼和小鱼相遇，大鱼会吃掉小鱼，体力恢复 20（最多恢复到 100）
# 当大鱼体力为 0，或小鱼的数量为 0 时，游戏结束
import random


class Fish:
    def __init__(self):  # 设置边界，生成位置
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)

    def move(self):
        if random.randint(0, 1):
            self.x += random.randint(-1, 1)
            self.x = self.set_real(self.x)  # 判断位置
        else:
            self.y += random.randint(-1, 1)
            self.y = self.set_real(self.y)  # 判断位置
        print(self.x, self.y)

    def set_real(self, o):
        if o > 10:
            return 9
        if o < 0:
            return 1
        return o


class BigFish(Fish):
    def __init__(self):
        super().__init__()
        self.hp = 100

    def move(self):
        self.x += random.randint(-1, 1)
        self.x = self.set_real(self.x)  # 判断位置
        self.y += random.randint(-1, 1)
        self.y = self.set_real(self.y)  # 判断位置
        print("大鱼:", self.x, self.y)

    def eat(self):
        self.hp += 20
        if self.hp > 100:
            self.hp = 100
        return big_fish.hp


class SmallFish(Fish):
    def __str__(self):
        return "fish at %d" %(self.x, self.y)
    pass


big_fish = BigFish()  # 创建大鱼对象

small_fishes = []
for i in range(10):  # 创建 10 个小鱼
    small_fishes.append(SmallFish())


eaten_fish = []
while big_fish.hp > 0 and small_fishes != []:
    big_fish.move()
    big_fish.hp -= 1
    for i, small_fish in enumerate(small_fishes):
        small_fish.move()
        if (big_fish.x, big_fish.y) == (small_fish.x, small_fish.y):
            big_fish.eat()
            eaten_fish.append(i)
    print("Big fish HP: %d" % (big_fish.hp))
    print(len(eaten_fish))
    for fish in eaten_fish:
        small_fishes.pop(fish)
    eaten_fish = []
    print("Theres only %d fishes left." % (len(small_fishes)))
if big_fish.hp <= 0:
    print("Small fish won")
else:
    print("Big fish won")
"""
em 这个代码可能会有bug，但是我真的不知道那个该怎么debug了
"""