def permutation(string, pocket=''):
    """Function to print all the permutations of a given string"""
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            current_letter = string[i]
            head = string[0:i]
            tail = string[i+1:]
            together = head + tail
            permutation(together, current_letter + pocket)


if __name__ == '__main__':
    permutation('ABC')
