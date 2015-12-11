import itertools

class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) + ', ' \
                 + str(self.weight) + '>'
        return result


def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book',
             'computer']
    vals = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    return Items


def dToB(n, numDigits):
    """requires: n is a natural number less than 2**numDigits
      returns a binary string of length numDigits representing the
              the decimal number n."""
    assert type(n) == int and type(numDigits) == int and 0 <= n < 2 ** numDigits
    bStr = ''
    while n > 0:
        bStr = str(n % 2) + bStr
        n //= 2
    while numDigits - len(bStr) > 0:
        bStr = '0' + bStr
    return bStr


def genPset_old(Items):
    """Generate a list of lists representing the power set of Items"""
    numSubsets = 2 ** len(Items)
    templates = []
    for i in range(numSubsets):
        templates.append(dToB(i, len(Items)))
    pset = []
    for t in templates:
        elem = []
        for j in range(len(t)):
            if t[j] == '1':
                elem.append(Items[j])
        pset.append(elem)
    return pset


def genPset(Items):
    """Generate a list of lists representing the power set of Items"""
    pset = []
    for i in range(len(Items) + 1):
        for s in itertools.combinations(Items, i):
            pset.append(s)

    return pset


Items = buildItems()
pset = genPset(Items)
print "There are %d sets" % len(pset)
for s in pset:
    print "Set contain %d items" % len(s)
    print "[",
    for i in s:
        print i.name,
        print ',',
    print "]"
