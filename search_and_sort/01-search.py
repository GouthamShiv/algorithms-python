def linear_search(array: list, target: int) -> int:
    """Linear search, finds and returns the position of the target value in the array"""
    for i in range(len(array)):
        if array[i] == target:
            return i+1
    return None


if __name__ == '__main__':
    arr = [2, 5, 8, 9, 10, 16, 22]
    target = 10
    print(linear_search(array=arr, target=target))
