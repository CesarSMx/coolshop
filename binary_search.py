import random


def binary_search(data, target, low_index, high_index):
    if low_index > high_index:
        return False
    mid = (low_index + high_index)//2 

    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data, target, low_index, mid-1)
    #elif target > data[mid]:
    else:
        return binary_search(data, target, mid + 1, high_index)

if __name__ == '__main__':
    #A list with 100 random numbers is created using list comprehension.
    data = [random.randint(1,100) for i in range(10)]
    data.sort()
    print(data)

    target = int(input('What number would you like to find? '))
    found = binary_search(data, target, 0, len(data) - 1)

    print(found)