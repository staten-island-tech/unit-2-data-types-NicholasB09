def hunger2(h, a, s):
    if a > h:
        a = h
    if a - s < 0:
        s = a
    print(a - s)
