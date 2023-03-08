def head(L):
    return L[0]
 
def tail(L):
    return L[1]

def py2ll(L):
    return (L[0], py2ll(L[1:])) if L else None

def ll2py(L):
    return [head(L)] + ll2py(tail(L)) if L else []

def size(L):
    return 1 + size(tail(L)) if L else 0

def sorted(L):
    return not L or not tail(L) or head(L) < head(tail(L)) and sorted(tail(L))

def sum(L):
    return head(L) + sum(tail(L)) if L else 0

def split(L):
    if not L:
        return None, None
    elif not tail(L):
        return None, L
    else:
        H0, H1 = head(L), head(tail(L))
        L0, L1 =  split(tail(tail(L)))
        return (H0, L0), (H1, L1)

def merge(L0, L1):
    if not L0:
        return L1
    elif not L1:
        return L0
    else:
        if head(L0) < head(L1):
            return (head(L0), merge(tail(L0), L1))
        else:
            return (head(L1), merge(L0, tail(L1)))

def mSort(L):
    if not L:
        return None
    else:
        L0, L1 = split(L)
        return merge(mSort(L0), mSort(L1))

def max(L):
    if not L:
        return None
    elif not tail(L):
        return head(L)
    else:
        curr_max = max(tail(L))
        return head(L) if head(L) > curr_max else curr_max

def get(L, N):
    return head(L) if N == 1 and L else get(tail(L), N - 1)
