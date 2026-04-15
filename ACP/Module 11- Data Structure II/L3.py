num = int(input("Enter your original number: "))

n = num
rev = 0

while n > 0:
    bit = n & 1          # get last bit
    rev = (rev << 1) | bit  # shift left and add bit
    n = n >> 1           # shift right

print("Reversed Number:", rev)