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
    def build(k):
        arr = [0 for _ in range(n)]
        arr[0],arr[1] = k[0],k[1]
        for i in range(2,n):
            arr[i] = 1 - arr[i-2]
        return arr
    
    def check(arr):
        for i in range(n):
            x = str(arr[i])
            if x==s[i] or s[i]=='?':
                continue
            return 0
        return 1
    
    ans = 0
    ops = [[0,0],[0,1],[1,0],[1,1]]
    for k in ops:
        ans += check(build(k))
    print(ans)