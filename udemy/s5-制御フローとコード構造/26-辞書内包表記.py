v = ["mon","tue","wed"]
f = ["co","mi","wat"]

## 通常の記法
d = {}
for x,y in zip(v,f):
    d[x] = y
print(d)

## 辞書内包表記
d = {x:y for x,y in zip(v,f)}
print(d)
