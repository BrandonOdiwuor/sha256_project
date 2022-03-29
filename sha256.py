def add32(*args):
    """
    Adds the numbers in the list of args and returns (sum % s ^ 32)
    """
    return sum(args) % (2**32)


def right_rotate32(value, count):
    """
    Bitwise right rotation of value by {count} places
    """
    assert value < 2 ** 32, "x is too large. Did you use + instead of add32 somewhere?"
    right_part = value >> count
    left_part = value << (32 - count)
    return add32(left_part, right_part)