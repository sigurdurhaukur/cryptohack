p = 857504083339712752489993810777
q = 1029224947942998075080348647219
totient = (p - 1)*(q - 1)
e = 65537

# find d, when ed = 1 mod totient
print(e, "d = 1 mod", totient )
