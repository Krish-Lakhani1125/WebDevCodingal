def rightmost_set_bit(n):
    return n & -n

# Taking input
num = int(input("Enter a number: "))

result = rightmost_set_bit(num)

print("Rightmost set bit value:", result)