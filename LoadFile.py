def LoadFile(b):
    with open(b, 'r') as openfile:
        print('OUTPUT', openfile.read())
