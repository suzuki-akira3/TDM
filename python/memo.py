from operator import methodcaller

text = '3x10^{-3}'
tups = ((a, '\\'+a) for a in '{}^')
for tup in tups:
    rep = methodcaller('replace', *tup)
    text = rep(text)
print(text)


from functools import partial

rep = methodcaller('replace', *tup)
rep2 = functools.partial(rep)
rep2('3x10^{-3}')