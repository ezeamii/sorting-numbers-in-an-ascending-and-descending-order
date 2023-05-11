# ARRANGING A LIST IN ASCENDING AND DESCENDING ORDER

list1 = []
n = int(input("How many numbers do you wish to input: "))

for i in range(1, n + 1):
    num = int(input(">>>"))
    list1.append(num)

print(list1)

list1.sort()
print("The list of numbers in ascending order is as follows: ", list1)

list1.sort(reverse=True)
print("The list of numbers in descending order is as follows: ", list1)