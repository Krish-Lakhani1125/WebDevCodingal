numberLargest = float(input("Enter a number:"))
numberSmallest = float(input("Enter another number:"))
largest = numberLargest
smallest = numberSmallest
while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print("HCF is : ", numberLargest)

hcf = numberLargest

lcm = (largest*smallest)/hcf
print("the Lowest Common Multiple is :", lcm)