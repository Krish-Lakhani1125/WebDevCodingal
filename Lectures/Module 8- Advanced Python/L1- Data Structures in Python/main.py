lst = ['apple', 'guava','mango','banana','kiwi']

print('length of list:', len(lst))
print('First Element:', lst[0])
print("Last Element:", lst[-1])

lst.append('papaya')
print("Updated List:",lst)

lst.remove("guava")
print("Updated Lit:", lst)

lst.sort()
print("Sorted List:", lst)

lst.pop(1)
print("Updated List:", lst)

lst.reverse()
print("Reversed List :", lst)
print("Multiplication on List :", lst)

lst = lst[:4]
print("Sliced List:", lst)
lst.clear()
print("updated list:", lst)