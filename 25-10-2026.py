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
    p = helper.read_ints()
    a = [0 for _ in p]
    for i in range(1,n-1):
        d1 = p[i]-p[i-1]
        d2 = p[i+1]-p[i]
        a[i] = (d2-d1)//2
    s = 0
    for i in range(1,n-1):
        s+=i*a[i]
    a[n-1] = (p[0]-s)//(n-1)
    s = 0
    for i in range(2,n):
        s+=(i-1)*a[i]
    a[0] = p[1]-s
    helper.print_arr(a)
    