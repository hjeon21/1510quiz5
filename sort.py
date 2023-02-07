def is_sorted(sorted_list):
    """
    confirm list is sorted

    :param sorted_list: a list
    :precondition: a list that contains any integers or is empty
    :postcondition: return a boolean value
    :return: a boolean value

    >>> is_sorted([1, 2, 3])
    True
    >>> is_sorted([3, 1, 2])
    False
    """
    if bool(sorted_list):
        if sorted_list == sorted(sorted_list):
            return True
        else:
            return False
    else:
        return False


def main():
    check_sorted = is_sorted([1, 2, 3, 4])
    print(check_sorted)


if __name__ == "__main__":
    main()
