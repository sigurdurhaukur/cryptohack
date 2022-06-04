def find_gcf(a, b):
    if a % b != 0:
        return find_gcf(b, a % b)
    else:
        return b

gcf = find_gcf(66528, 52920)
print(gcf)
