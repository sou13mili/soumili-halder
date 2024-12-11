import itertools

def generate_permutations(input_list):
    """
    Generate all permutations of a given list.

    :param input_list: List of elements to permute.
    :return: List of permutations.
    """
    return list(itertools.permutations(input_list))

# Example usage
if __name__ == "__main__":
    my_list = [1, 2, 3]
    permutations = generate_permutations(my_list)
    print("Permutations:")
    for perm in permutations:
        print(perm)
