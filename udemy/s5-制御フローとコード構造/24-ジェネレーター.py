l = ["good morning","good afternoon","good night"]

for i in l :
    print(i)

print("##############")

def greeting():
    yield "good morning"
    yield "good afternoon"
    yield "good night"

## nextで一つずつ表示させることができ、間に他の処理を書くことができる
g = greeting()
print(next(g))
print("###")
print(next(g))
print("###")
print(next(g))

# for g in greeting():
#     print(g)