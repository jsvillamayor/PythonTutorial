# numbers = [1,2,3,4,5,19,3]
# numbers2 = numbers.copy()
# numbers.pop()
# print(numbers2)
numbers = [1,1,2,3,3,4,4,4,4,5,6,2,11]
finalNumbers = []
for item in numbers:
    if item not in finalNumbers:
        finalNumbers.append(item)
print(finalNumbers)
