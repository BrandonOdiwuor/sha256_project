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


def little_sigma0(x):
    """
    s0 := (x rightrotate  7) xor (x rightrotate 18) xor (x rightshift  3)
    """
    return right_rotate32(x, 7) ^ right_rotate32(x, 18) ^ x >> 3


def little_sigma1(x):
    """
    s1 := (x rightrotate 17) xor (x rightrotate 19) xor (x rightshift 10)
    """
    return right_rotate32(x, 17) ^ right_rotate32(x, 19) ^ x >> 10
