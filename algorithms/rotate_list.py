def rotate_list(l, k=1):
    return [*l[-k:], *l[:len(l)-k]]