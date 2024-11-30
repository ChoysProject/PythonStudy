def gugu(i, num):
    print("%d x %d = %2d" % (num, i, dan * num), end=" | ")
    if num < 9:
        gugu(dan, num + 1)


for dan in range(1, 10):
    # print("## %d단 ##" % dan)
    gugu(dan, 2)
    print()