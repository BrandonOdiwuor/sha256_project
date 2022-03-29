from .sha256 import add32, right_rotate32, little_sigma0, little_sigma1


def test_add32_one():
    assert add32(1, 2, 4) == 7

def test_add32_two():
    assert add32(4294967295, 1) == 0

def test_add32_three():
    assert add32(3050487260, 3710144918) == 2465664882

def test_right_rotate32_one():
    assert right_rotate32(2, 1) == 1

def test_right_rotate32_two():
    assert right_rotate32(1, 1) == 2147483648

def test_right_rotate32_three():
    assert right_rotate32(2919882184, 31) == 1544797073

def test_little_sigma0():
    assert little_sigma0(1114723206) == 1345017931

def test_little_sigma1():
    assert  little_sigma1(1232674167) == 2902922196