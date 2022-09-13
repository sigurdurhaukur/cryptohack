
# the givens
p = 29
ints = [14, 6, 11]
# 14 mod 29

a = 1



# loop over plausable quadratic residue
for _int in ints:
    # check if it is a quadratic residue
    quadratic_residue = None
    square_roots = []
    for a in range(p-1):

        # if it's a quadratic residue, calculate it's roots
        if(a**2  % p == _int % p):
            quadratic_residue = _int
            square_roots.append(a)  

        # if both square roots are found stop calculating 
        if(len(square_roots) == 2):
            print("quadratic residue: ", quadratic_residue)
            print("square roots: ", square_roots)
            print("\nsolution: ", min(square_roots))
            break

        a += 1
