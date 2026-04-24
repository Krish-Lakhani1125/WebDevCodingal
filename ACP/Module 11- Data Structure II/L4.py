def is_power_of_8(n):
    # Step 1: n must be positive and a power of 2
    if n <= 0 or (n & (n - 1)) != 0:
        return False
    
    # Step 2: check if the position of the only set bit is multiple of 3
    return (n.bit_length() - 1) % 3 == 0


# Input from user
num = int(input("Enter a number: "))

if is_power_of_8(num):
    print(f"{num} is a power of 8")
else:
    print(f"{num} is NOT a power of 8")