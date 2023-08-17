def fun1():
    for i in range(2,10):
        for j in range(1,10):
            print(i, "x", j, "=", i * j)

def fun2():
    for i in range(2,10):
        print(i,"단")
        for j in range(1,10):
            print(i, "x", j, "=", i * j, end="  ")
        print()