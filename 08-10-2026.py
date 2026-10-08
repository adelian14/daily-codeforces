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
    s = helper.read_line()
    if s[0]=='1':
        print(s.count('0'))
        continue
    a = [0]+[int(x) for x in s]
    for i in range(1,n+1):
        a[i]+=a[i-1]
    ans = min(s.count('0'),s.count('1'))
    for i in range(1,n+1):
        len_zeros = i-1
        len_ones = n-len_zeros
        cnt_zeros = len_zeros-a[i-1]
        cnt_ones = a[n]-a[i-1]
        ones = 10**9
        zeros = len_zeros-cnt_zeros
        if a[i] > 0:
            ones = len_ones-cnt_ones
        ans = min(ans,ones+zeros)
    print(ans)