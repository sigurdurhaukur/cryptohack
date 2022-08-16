p = 857504083339712752489993810777
q = 1029224947942998075080348647219
totient = (p - 1)*(q - 1)
e = 65537


# the extended Euclidean Algorithm
def gcdExtended(a, b):
    # Base Case
    if a == 0 :
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a)
     
    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1
     
    #    ax + by = gcd(a, b)
    return gcd,x,y
     
 

# calculate the modular multiplicative inverse of e
def modular_multiplicative_inverse(a, n):
        gcd, x ,y = gcdExtended(a, n)
        return x % n


flag = modular_multiplicative_inverse(e, totient)
print(flag)