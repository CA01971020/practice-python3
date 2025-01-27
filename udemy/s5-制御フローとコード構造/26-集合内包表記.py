s = set()

## 通常記法
for i in range(10):
    s.add(i)
print(s)

## 集合内包表記
s = {i for i in range(10)}
print(s)