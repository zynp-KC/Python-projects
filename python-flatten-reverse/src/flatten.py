def flatten(l):
    new_list = []
    for i in l:
        if isinstance(i, list):
            new_list.extend(flatten(i))
        else:
            new_list.append(i)
    return new_list