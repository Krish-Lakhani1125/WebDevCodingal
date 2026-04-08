def circuit_output(A, B, C):
    Q = (A and B) or (B and C)
    return int(Q)

# Test all combinations
print("A B C | Q")
for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            print(A, B, C, "|", circuit_output(A, B, C))