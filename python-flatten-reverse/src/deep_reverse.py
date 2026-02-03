def deep_reverse(l):
    l.reverse()
    for i in l:
        if isinstance(i, list):
            deep_reverse(i)
    return l