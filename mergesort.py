# a is array
def merge(a: list, l: int, m: int, r: int):
    n1: list = a[l:m+1]
    n2: list = a[m+1:r]
    a[l:r+1] = sorted([n1.append(n2)])

def mergesort(a: list, l: int, r: int):
    if (l < r):
        m = (l + r) // 2
        mergesort(a, l, m)
        mergesort(a, m + 1, r)
        merge(a, l, m, r)
