import enum

#dbにデータを格納する場合、文字列より整数のほうが処理が早い
db = {
    "stack1":1,
    "stack2":2,
}

# 例
# STATUS_ACTIVE = 1
# STATUS_INACTIVE = 2

# if db["stack1"] == STATUS_ACTIVE:
#     print("shutdown")
# elif db["stack1"] == STATUS_INACTIVE:
#     print("terminate")

# Enumを使う場合の例1
class Status(enum.Enum):
    ACTIVE = 1
    INACTIVE = 2
    RUNNING = 3

## stack1
if Status(db["stack1"]) == Status.ACTIVE:
    print("shutdown")
elif Status(db["stack1"]) == Status.INACTIVE:
    print("terminate")

print("---------")

## stack2
if Status(db["stack2"]) == Status.ACTIVE:
    print("shutdown")
elif Status(db["stack2"]) == Status.INACTIVE:
    print("terminate")