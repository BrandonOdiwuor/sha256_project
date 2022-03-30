ROUND_CONSTANTS = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
]

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


def majority(x, y, z):
    """
    Maj(x, y, z) = (x AND y) XOR (x AND z) XOR (y AND Z)
    """
    return (x & y) ^ (x & z) ^ (y & z)


def round(state, round_constant, schedule_word):
    _choice = choice(state[4], state[5], state[6])
    s1 = big_sigma1(state[4])
    temp1 = add32(state[7], s1, _choice, round_constant, schedule_word)
    _majority = majority(state[0], state[1], state[2])
    s0 = big_sigma0(state[0])
    temp2 = add32(s0, _majority)

    return [
        add32(temp1, temp2),
        state[0],
        state[1],
        state[2],
        add32(state[3], temp1),
        state[4],
        state[5],
        state[6]
    ]


def compress(input_state, block):
    w = message_schedule_array(block)
    state = input_state

    for i in range(64):
        state = round(state, ROUND_CONSTANTS[i], w[i])
    
    return [add32(state, _input_state) for state, _input_state in zip(state, input_state)]


def padding(message_length):
    remaining_bytes = (message_length + 8) % 64
    filler_bytes = 64 - remaining_bytes
    zero_bytes = filler_bytes - 1
    encoded_length = (message_length * 8).to_bytes(8, 'big')
    return b"\x80" + b"\0" * zero_bytes + encoded_length
