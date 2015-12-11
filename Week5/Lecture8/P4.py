def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list
        of which item(s) are in each bag.
        :param items: list
    """
    # Your code here
    n = len(items)
    # enumerate the 3**N possible combinations
    for i in xrange(3**n):
        combo1 = []
        combo2 = []
        for j in xrange(n):
            if (i / (3 ** j)) % 3 == 1:
                combo1.append(items[j])
            elif (i / (3 ** j)) % 3 == 2:
                combo2.append(items[j])
        yield (combo1, combo2)
