s = """\
AAA
BBB
CCC
DDD
"""

# write
with open("test.txt","w") as f :
    f.write(s)
    print("03-read-file",file=f)

# read
with open("test.txt","r") as f :

    # f.readで一気に全てを読み込む
    # print(f.read())

    #while文で一行ずつ出力することも可能
    while True:
        # chunk = 2
        line = f.readline()
        print(line,end="")
        if not line:
            break

    #chunkで文字数を指定することも可能
    # while True:
    #     chunk = 2
    #     line = f.read(chunk)
    #     print(line)
    #     if not line:
    #         break