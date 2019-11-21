def Union(o,p):
    ino = set(o)
    inp = set(p)
    inop = inp - ino
    sol = o + list(inop)
    print('OUTPUT', sol)
