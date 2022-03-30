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


def message_schedule_array(block):
    assert len(block) == 64
    w = []
    for i in range(64):
        if i < 16:
            assert i == len(w)
            w.append(int.from_bytes(block[i * 4: i * 4 + 4], 'big'))
        else:
            s0 = little_sigma0(w[i - 15])
            s1 = little_sigma1(w[i - 2])
            w.append(add32(w[i-16], s0, w[i-7], s1))
    return w


def big_sigma0(word):
    """
    E0 := (x rightrotate 2) xor (x rightrotate 13) xor (x rightrotate 22)
    """
    return right_rotate32(word, 2) ^ right_rotate32(word, 13) ^ right_rotate32(word, 22)


def big_sigma1(word):
    """
    E1 := (x rightrotate 6) xor (x rightrotate 11) xor (x rightrotate 25)
    """
    return right_rotate32(word, 6) ^ right_rotate32(word, 11) ^ right_rotate32(word, 25)


def choice(x, y, z):
    """
    ch(e,f,g) = (e AND f) xor (not e AND z)
    """
    return (x & y) ^ (~x & z)
