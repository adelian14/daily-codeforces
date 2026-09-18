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
    n,m = helper.read_ints()
    a = helper.read_ints()
    idx = {}
    p = [-1 for _ in a]
    for i,x in enumerate(a):
        if x not in idx:
            idx[x] = []
        idx[x].append(i)
    a = [[k,v] for k,v in idx.items()]
    a.sort()
    last = -1
    for _,k in a:
        cnt = len(k)
        i = last + cnt
        for x in k:
            p[i]=x
            i-=1
        last+=cnt
    ans = 0
    for i in range(m):
        for j in range(i):
            if p[j] < p[i]:
                ans+=1
    print(ans)