t = [1,2,3,4,5]

## 簡単なfor文
r1 = []
for i in t:
    if i % 2 == 0:
        r1.append(i)
print(r1)

## リスト内包表記は簡単な処理のみ書く
r2 = [i for i in t if i % 2 == 0]
print(r2)