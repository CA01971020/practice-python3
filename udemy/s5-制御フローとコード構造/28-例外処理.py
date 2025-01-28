l = [ 1 , 2 , 3]
i = 5

# try文がないと、エラーとなったときに以降のプログラムが動作しない
try:
    l[i]
## index error の時だけという指定もできる
except IndexError as ex:
    print("don't worry:{}".format(ex))
except NameError as ex:
    print(ex)
## 自分が意図しないものをキャッチするときはExceptionだが、あまり良いコードではない
except Exception as ex:
    print("other{}".format(ex))
## exceptが問題なく抜けたらelseを実行する（try-else文）
else:
    print("done")
## try で何が起きても、finallyは絶対に実行する
finally:
    print("clean up")

print("last")