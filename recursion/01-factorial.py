def iterative_factorial(n: int) -> int:
    """Get the factorial of a number in iterative way"""
    factorial = 1
    for idx in range(2, n+1):
        factorial *= idx
    return factorial


def recursive_factorial(n: int) -> int:
    """Get the factorial of a number in recursive way"""
    if n == 1:
        return n
    else:
        temp = recursive_factorial(n-1)
        temp *= n
    return temp


if __name__ == '__main__':
    print(f'Iterative factorial of 6: {iterative_factorial(6)}')
    print(f'Recursive factorial of 5: {recursive_factorial(5)}')
