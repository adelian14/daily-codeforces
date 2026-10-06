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
    hr,m = helper.read_ints()
    h,d,c,n = helper.read_ints()
    k = hr*60+m
    p = 20*60
    if k >= p:
        print(((h+n-1)//n)*(c*.8))
        continue
    ans = ((h+n-1)//n)*c*1.0
    diff = p-k
    h+=(diff*d)
    ans2 = ((h+n-1)//n)*(c*.8)
    print(min(ans,ans2))
    
    
    