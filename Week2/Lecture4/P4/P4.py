def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if not L:
        return float('NaN')

    size = len(L)
    total_size = 0.0
    for strInL in L:
        total_size += len(strInL)

    mean = total_size/size
    tot = 0.0

    for strInL in L:
        tot += (len(strInL) - mean) ** 2

    deviation = (tot / size) ** 0.5

    return deviation
