def add32(*args):
    """
    Adds the numbers in the list of args and returns (sum % s ^ 32)
    """
    return sum(args) % (2**32)