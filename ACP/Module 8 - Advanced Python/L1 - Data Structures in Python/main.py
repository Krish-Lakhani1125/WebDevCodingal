fruits = ["apple", "banana", "cherry", "date"]

print("Original list of fruits:", fruits)

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

fruits[1] = "blueberry"
print("List after modifying an element:", fruits)

fruits.append("elderberry")
print("List after appending an element:", fruits)

fruits.remove("cherry")
print("List after removing an element:", fruits)
