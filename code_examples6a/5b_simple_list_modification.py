def squareTheList(numbers):
    for i in range(0, len(numbers)):
        numbers[i] = numbers[i] * numbers[i]

n = [1,2,3,4,5,6]

print(n)
squareTheList(n)
print(n)

