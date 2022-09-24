from math import factorial


def permutation_recursive(string: str, pocket='') -> None:
    """Recursive function to print all the permutations of a given string"""
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            current_letter = string[i]
            head = string[0:i]
            tail = string[i+1:]
            together = head + tail
            permutation_recursive(together, current_letter + pocket)


def permutation_iterative(string: str) -> None:
    """Iterative function to print all the permutations of a given string"""
    for p in range(factorial(len(string))):
        print(''.join(string))
        i = len(string) - 1
        while i > 0 and string[i - 1] > string[i]:
            i -= 1
        string[i:] = reversed(string[i:])
        if i > 0:
            q = i
            while string[i - 1] > string[q]:
                q += 1
            temp = string[i - 1]
            string[i - 1] = string[q]
            string[q] = temp


if __name__ == '__main__':
    permutation_recursive('ABC')
    permutation_iterative(list('ABC'))
