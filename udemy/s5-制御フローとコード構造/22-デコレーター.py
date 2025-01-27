def print_info(func):
    def wrapper(*args,**kwargs):
        print("start")
        result = func(*args,**kwargs)
        print("end")
        return result
    return wrapper

## デコレーターは@関数で作る
@print_info
def add_num(a,b):
    return a + b

ar = add_num(10,20)
print(ar)

## デコレーターを呼び出せば、使用することができる
@print_info
def sub_num(a,b):
    return a - b

sr = sub_num(10,20)
print(sr)

# f = print_info(add_num)
# r = f(10,20)
# print(r)

# print("start")
# r = add_num(10,20)
# print("end")

# print(r)