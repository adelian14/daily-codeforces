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
    k = []
    ones = s.count('1')
    zeros = n-ones
    for x in s:
        if len(k)==0 or x!=k[-1]:
            k.append(x)
            
    len_ones = len(k)
    len_zeros = len(k)
    if k[0]=='1':
        len_zeros-=1
    else:
        len_ones-=1
    ans = 10**9
    for m in range(1, len_ones+1):
        cnt_ones = m//2+m%2
        cnt_zeros = m//2
        ones_removed = ones-cnt_ones
        zeros_removed = zeros-cnt_zeros
        if abs(ones_removed-zeros_removed) < 2:
            ans = min(ans,ones_removed+zeros_removed)
    
    for m in range(1, len_zeros+1):
        cnt_ones = m//2
        cnt_zeros = m//2+m%2
        ones_removed = ones-cnt_ones
        zeros_removed = zeros-cnt_zeros
        if abs(ones_removed-zeros_removed) < 2:
            ans = min(ans,ones_removed+zeros_removed)
    if ans > n:
        ans = -1
    print(ans)
    