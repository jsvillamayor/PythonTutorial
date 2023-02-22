# names = ['James', 'Daniel', 'Karina', 'Christine']
# print(names[:1])
numbers = [1,4,56,123,5,47]
answer = numbers[0]
for item in numbers:
    if item > answer:
        answer = item
print(answer)