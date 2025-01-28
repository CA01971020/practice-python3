# raise IndexError ("test error")

## Exceptionを継承して、UppercaseErrorクラスを作成
class UppercaseError(Exception):
    pass

def check():
    words = ["APPLE","orange","banana"]
    for word in words:
        if word.isupper():
            ## 独自の例外処理を作成できる
            raise UppercaseError(word)

try:
    check()
except UppercaseError as exc:
    print("this is my fault go next")