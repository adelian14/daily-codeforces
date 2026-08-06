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
    a = helper.read_ints()
    cnt = {}
    mx = 0
    for x in a:
        if x not in cnt: cnt[x] = 0
        cnt[x]+=1
        mx = max(mx,x)
    arr = [mx]
    cnt[mx]-=1
    a = [[k,v] for k,v in cnt.items() if v]
    a.sort()
    for i in range(len(a)):
        k,v = a[i]
        arr.append(k)
    mex = 0
    ans = 0
    for i in range(n):
        if i < len(arr):
            if mex==arr[i]:
                mex+=1
            if mex==mx:
                mex+=1
        ans += mx+mex
    print(ans)