from .sha256 import add32, right_rotate32, little_sigma0, little_sigma1, message_schedule_array,\
    big_sigma0, big_sigma1


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

def test_message_schedule_array():
    block = "iguana wombat dog kangaroo llama turkey yak unicorn sheep xenoce"
    message_schedule = [
        1768387937, 1851859063, 1869439585, 1948279919, 1730177889, 1852268914, 1869553772, 1818324321,
        544503154, 1801812256, 2036427552, 1970170211, 1869770272, 1936221541, 1881176165, 1852793701,
        3002878561, 3711121932, 1520676164, 3002441970, 2935068969, 1610329529, 1904580351, 3219988740,
        2337695268, 263015313, 2120931855, 131203777, 3818546915, 19163115, 3479924161, 2154860703,
        1790169326, 516580487, 2414737634, 909025701, 2241053595, 1237268359, 3797503938, 1773623028,
        2840671725, 2299292186, 1933596460, 2279513616, 514132674, 3245155609, 1753922983, 2241450350,
        2449659630, 262239956, 773552098, 3253131632, 3863807927, 879696536, 3143654396, 3973063648,
        509015903, 270850193, 1893431553, 719566283, 2310657204, 365781698, 3761063438, 1007484868
    ]
    assert message_schedule_array(block.encode()) == message_schedule

def test_big_sigma0():
    assert big_sigma0(3536071395) == 3003388882

def test_big_sigma1():
    assert big_sigma1(651015076) == 2194029931