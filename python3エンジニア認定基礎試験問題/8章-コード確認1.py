fp = open("test.txt")
for s in fp:
    print(s)

print("----------")

fp = open("test.txt")
for s in fp.readlines():
    print(s)

print("----------")

fp = open("test.txt")
for s in list(fp):
    print(s)