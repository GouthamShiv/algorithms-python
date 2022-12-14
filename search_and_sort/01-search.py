def linear_search(array: list, target: int) -> int:
    """Linear search, finds and returns the position of the target value in the array"""
    for i in range(len(array)):
        if array[i] == target:
            return i+1
    return None


def binary_search_iterative(array: list, start: int, end: int, target: int) -> int:
    """Binary search - iterative, finds and returns the position of the target value in the array\n
    Usually works on sorted array"""
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid + 1
        elif arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            return None


def binary_search_recursive(array: list, start: int, end: int, target: int) -> int:
    """Binary search - recursive, finds and returns the position of the target value in the array\n
    Usually works on sorted array"""
    if start > end:
        return None
    else:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid + 1
        elif array[mid] < target:
            return binary_search_recursive(array, mid + 1, end, target)
        else:
            return binary_search_recursive(array, start, mid - 1, target)


if __name__ == '__main__':
    arr = [2, 5, 8, 9, 10, 16, 22]
    target = 5
    print(
        f'Linear Search - for target {target} in array {arr} is in position: {linear_search(array=arr, target=target)}')
    print(
        f'Binary Search - Iterative for target {target} in array {arr} is in position: {binary_search_iterative(array=arr, start=0, end=len(arr)-1, target=target)}')
    print(
        f'Binary Search - Recursive for target {target} in array {arr} is in position: {binary_search_recursive(array=arr, start=0, end=len(arr)-1, target=target)}')
