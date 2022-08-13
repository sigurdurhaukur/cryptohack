
# the givens
p = 29
ints = [14, 6, 11]

x = 1

# loop over each constant
for _int in ints:
    # check if it is a quadratic residue
    for x in range(p-1):
        # if a quadratic residue exist print it!
        if(x ** 2 == _int % p):
            print(x * -1, x)

        x += 1
