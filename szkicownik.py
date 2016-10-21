import re

def getWords(text):
    return re.compile('\w+').findall(text)


data_to_compare = (''.join([c for c in "LOVE ME BY *" if c not in ('_', '* ', '*')]))

# with_star = "LOVE ME BY *"
with_star = "WOJNA WOJNA KURCZAK BOMBA _"
to_stared = "LOVE ME BY BOND KOK"
with_star = getWords(with_star)
to_stared = getWords(to_stared)
temp3 = [x for x in (to_stared) if x not in (with_star)]
print("temp3 :" + str(temp3))



########################
print (((''.join([c for c in "kokd...K.!" if c not in (',', '.', '?', '!')]))).upper())

def getWords(text):
    return re.compile('\w+').findall(text)
def subtract_lists(a, b):
    """ Subtracts two lists. Throws ValueError if b contains items not in a """
    # Terminate if b is empty, otherwise remove b[0] from a and recurse
    return a if len(b) == 0 else [a[:i] + subtract_lists(a[i+1:], b[1:])
                                  for i in [a.index(b[0])]][0]

ggg = "LOVE ME BY BOND"
www = "KOKO WINO SPIEW"
kkk = "LOVE ME BY * "
k = getWords(kkk)
hohohoh = getWords(ggg)
print(k)
print(hohohoh)
print len(set(k) & set(hohohoh)) >= min(len(k), len(hohohoh))
print " ".join(subtract_lists(hohohoh, k))