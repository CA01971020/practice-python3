# リストだと検索が面倒
l = [
    ["apple",10],
    ["banana",20],
    ["orange",30],
]
print(l[0][1],"dollar")

# 辞書型だと検索が簡単
# ハッシュテーブルなので取り出しスピードも早い
fruits = {
    "apple":10,
    "banana":20,
    "orange":30,
}

print(fruits["apple"],"dollar")