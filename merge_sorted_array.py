def mergeSortedArrays(arr1, arr2):
    new_array = arr1 + arr2
    new_array.sort()

    return new_array


if __name__ == '__main__':
    array_1 = [0, 3, 4, 31]
    array_2 = [4, 6, 30]

    print(mergeSortedArrays(array_1, array_2))
