def get_substrings(s):
    substrings = []
    n = len(s)
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.append(s[i:j])
    
    return substrings


# Taking input from user
user_input = input("Enter a string: ")

result = get_substrings(user_input)

print("All substrings are:")
for sub in result:
    print(sub)