# 5.2.9 编写一个函数，功能是计算单人跳水比赛中的一次得分
# 单人项目跳水比赛时由 7 名裁判员分坐在跳台两侧的池岸上评分，最高 10 分，失败 0 分。
# 在计算分数时，去掉 2 个最高分和 2 个最低分，将 3 个中间分数相加之和，乘以动作的难度系数，就是动作的最终得分
import random


def final_score(score):
    global item # 这个是python给我推荐的，我不太明白这个是什么意思
    score = list(score)
    score.sort()
    score.pop(0)
    score.pop(0)
    score.pop()
    score.pop()
    for item in score:
        item += item
    difficulties = random.randint(5, 10)
    item *= difficulties
    return item


score = [7, 7, 9, 10, 8, 6, 8]
print(final_score(score))

