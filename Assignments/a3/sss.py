def rec(x):
    if x==1:
        return x
    else:
        return rec(x-1)*x
