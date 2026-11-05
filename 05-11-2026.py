import os
from collections import defaultdict

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
freqs = [0 for _ in range(10**5)]
for _ in range(t):
    n = helper.read_int()
    a = helper.read_ints()
    vals = []
    for i in range(n-4):
        vals.append(a[i]+a[i+2]-a[i+4]+30005)
    ans = 0
    for i,x in enumerate(vals):
        cnt = freqs[x]
        if i >= 2 and vals[i-2]==x:
            cnt-=1
        if i >= 4 and vals[i-4]==x:
            cnt-=1
        ans += cnt
        freqs[x] += 1
        
    for x in vals:
        freqs[x] = 0
        
    print(ans)