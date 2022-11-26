def IPv4(n):
    n_2=''.  join(bin(n)[2:])
    s='0'*(32-len(n_2))+n_2
    l = [('0'*(32-len(n_2))+n_2)[i * 8:(i + 1) * 8] for i in range(4)]
    return '.'.join([str(int(i, 2)) for i in l])

