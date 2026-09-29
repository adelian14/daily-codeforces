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

t = 1 # helper.read_int()
for _ in range(t):
    n = helper.read_int()
    if n==1:
        print(1)
        print(1,1)
        continue
    for x in range(1,1000):
        if (x-1)*2 >= n-1:
            ans = x
            break
    print(ans)
    idx = 1
    for i in range(1,ans+1):
        print(1,i)
        idx+=1
        if idx > n:
            break
    if idx > n:
        continue
    for i in range(2,ans+1):
        print(ans,i)
        idx+=1
        if idx > n:
            break