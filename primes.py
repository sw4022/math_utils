def isprime(n):
    for v in range(1,n,1):
        if n%v == 0:
            return False
    return True

        
