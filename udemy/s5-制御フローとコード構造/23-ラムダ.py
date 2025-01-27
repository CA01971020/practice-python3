## 小文字と大文字混じりのリスト
l = ["Mon","tue","Wed","Thu","fri","sat","sun"]

def change_words(words,func):
    for word in words:
        print(func(word))

# def sample_func1(word):
#     # キャピタライズは単語の頭文字を大文字にすること
#     return word.capitalize()

# ## リストlの中身をキャピタライズして表示
# change_words(l,sample_func1)

## ラムダを使うことで簡単にできる
# sample_func2 = lambda word:word.capitalize()
# change_words(l,sample_func2)

change_words(l,lambda word:word.capitalize())

change_words(l,lambda word:word.lower())