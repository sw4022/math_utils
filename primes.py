def isprime(n):
    if n == 1:
            return False
    for v in range(2,n):
        if n%v == 0 and n!=1:
            return False
    return True

        
