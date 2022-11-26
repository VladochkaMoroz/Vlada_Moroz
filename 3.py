def digital_root(n):
    if n > 10:
        return digital_root(sum([int(i) for i in str(n)]))
    else:
        return n
