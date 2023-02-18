def making_factorials(n):
    if n==1:
        return n
    return(n*making_factorials(n-1))

print(making_factorials(6))

