def ScoreFinder(h,l,m):
    h = h.lower()
    index1 = h.index(m)
    if h[m] == m:
        print('OUTPUT', h[m], 'got a score of', l[m])
    else:
        print('OUTPUT player not found')
