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

t = 1#helper.read_int()
for _ in range(t):
    n = helper.read_int()
    s = helper.read_line()
    def solve(k):
        ans = 0
        a = 'ACTG'
        for x,y in zip(k,a):
            ans += min(abs(ord(x)-ord(y)), ord('Z')-ord(x)+1+ord(y)-ord('A'), ord(x)-ord('A')+1+ord('Z')-ord(y))
        return ans
    ans = 10**9
    for i in range(n-3):
        ans = min(ans,solve(s[i:i+4]))
    print(ans)