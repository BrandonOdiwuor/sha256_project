import argparse

from sha256.constants import ROUND_CONSTANTS, INITIALIZATION_VECTOR


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


def sha256(message):
    message_blocks = message + padding(len(message))
    state_words = INITIALIZATION_VECTOR
    for block_start_index in range(0, len(message_blocks), 64):
        block = message_blocks[block_start_index:block_start_index + 64]
        state_words = compress(state_words, block)

    return b"".join(x.to_bytes(4, 'big') for x in state_words)


def main():
    parser = argparse.ArgumentParser(description='Hashes a string or a file using the sha-256 algorithm')
    parser.add_argument('--string', '-s', help='a string to be hashed')
    parser.add_argument('--file', '-f', help='a file to be hashed')
    args = parser.parse_args()

    message = ""
    if args.string:
        message = args.string.encode()
    if args.file:
        with open(args.file) as file:
            message = file.read().encode()
    digest = sha256(message)
    print(digest.hex())


if __name__ == "__main__":
    main()
    