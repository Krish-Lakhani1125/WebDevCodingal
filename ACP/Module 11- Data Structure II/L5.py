def longest_consecutive_ones(n):
    count = 0
    while n:
        n = n & (n << 1)
        count += 1
    return count


# Input from user
num = int(input("Enter a number: "))

result = longest_consecutive_ones(num)
print("Longest consecutive 1's:", result)