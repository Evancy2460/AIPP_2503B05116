numbers=[1,2,3]
try:
    print(numbers[5])
except IndexError:
    print("Index out of range")