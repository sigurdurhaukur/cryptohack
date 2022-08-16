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
     
 

# calculate the gcd of p and q
gcd, x ,y = gcdExtended(e, totient)
print(gcd, x, y)

print(x % totient)
# find d, when ed = 1 mod totient
# calculate the modular multiplicative inverse of e


print(e, "d = 1 mod", totient )
