def g():
    for i in range(10):
        yield i

## 通常表記
g = g()
print(type(g))
print(next(g))

## ジェネレーター内包表記
g = (i for i in range(10))
print(type(g))
print(next(g))