"""Print out all possible candidates. Assuming words
with only consonants are not legal and words with 4
times the same vocal not legal."""
def xor(a,b):
    return (not a) ^ (not b)
i = 0
for a in 'HIONSXZ':
    for b in 'HIONSXZ':
        if xor(a in 'IO',  b in 'IO'):
            word =  a + b + b + a
            i+=1
            print "%2i %s " % (i, word)
