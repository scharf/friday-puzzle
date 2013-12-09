i = 0
for c in 'IO':
    for v in 'HNSXZ':
        i += 1
        print "%2i %s " % (i, v + c + c + v)
        i += 1
        print "%2i %s " % (i, c + v + v + c)
for c in 'IO':
    for v in 'IO':
        if c != v:
            i += 1
            print "%2i %s " % (i, v + c + c + v)
