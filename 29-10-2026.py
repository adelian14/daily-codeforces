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
                
helper = TestcaseHelper()

t = helper.read_int()
for _ in range(t):
    n = helper.read_int()
    ans = "NO"
    s = ''
    while n:
        s = str(n%2)+s
        n//=2
    if not s:
        s = '0'
    for length in range(1,64):
        if length <  len(s):
            continue
        p = '0' * (length - len(s)) + s
        is_pal = False
        if p==p[::-1]:
            is_pal = True
        zero_mid = True
        if length % 2 == 1:
            mid = length // 2
            if p[mid] == '1':
                zero_mid = False
        if is_pal and zero_mid:
            ans = "YES"
            break
    print(ans)
    
    
    