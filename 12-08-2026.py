import os

class TestcaseHelper:
    def __init__(self):
        self.local_env = True
        self.input_lines = None
        self.current_index = -1
        testcases_path = '_codeforces_testcases.txt'
        if os.path.exists(testcases_path):
            with open(testcases_path,"r") as f:
                s = f.read()
            self.input_lines = s.split('\n')
        else:
            self.local_env = False
    
    def read_line(self):
        if self.local_env:
            self.current_index+=1
            return self.input_lines[self.current_index]
        return input()
    
    def read_int(self):
        return int(self.read_line())
    
    def read_float(self):
        return float(self.read_line())
    
    def read_ints(self):
        line = self.read_line()
        return [int(x) for x in line.split()]
    
    def read_floats(self):
        line = self.read_line()
        return [float(x) for x in line.split()]
    
    def read_strs(self, sep = ' '):
        line = self.read_line()
        return [x for x in line.split(sep=sep)]
    
    def print_arr(self, arr):
        print(' '.join([str(x) for x in arr]))
                

def common_prefix(a, b):
    la = a.bit_length()
    lb = b.bit_length()

    l = min(la, lb)

    a >>= la - l
    b >>= lb - l

    diff = a ^ b

    if diff == 0:
        return a

    common = l - diff.bit_length()

    return a >> (l - common)

helper = TestcaseHelper()

t = helper.read_int()
for _ in range(t):
    n = helper.read_int()
    a = helper.read_ints()
    depth = 0
    ones = 0
    prefix = None
    min_len = 10**9
    for x in a:
        if x == 1:
            ones += 1
            continue
        y = x - 1
        length = y.bit_length()
        depth += 2 * length - y.bit_count()
        min_len = min(min_len, length)
        if prefix is None:
            prefix = y
        else:
            prefix = common_prefix(prefix, y)

    if ones:
        cost_1 = depth
        cost_2 = depth - (n - ones) + ones

        ans = min(cost_1, cost_2)

    else:
        if min_len == prefix.bit_length():
            anc_y = prefix
        else:
            anc_y = (prefix << 1) | 1

        length = anc_y.bit_length()
        anc_depth = 2 * length - anc_y.bit_count()
        ans = depth - n * anc_depth

    print(ans)