class A:
    def __init__(self):
        self.b = 1
        del self


a = A()
print(a.b)


def test(n):
    del n


n = 1
test(n)
print(n)
"""
因为是在函数内部删除的，所以对外界不会产生影响，（可能是这个意思吧）
"""
