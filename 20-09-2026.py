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
    n,m = helper.read_ints()
    s = helper.read_line()
    t = helper.read_line()
    mn = 10**9
    bounds = [-1,-1]
    for i in range(0,m-n+1):
        cnt = 0
        for x,y in zip(s,t[i:i+n]):
            if x!=y:
                cnt+=1
                if cnt >= mn:
                    break
                
        if cnt < mn:
            mn = cnt
            bounds = [i,i+n]
    print(mn)
    ans = []
    for i,item in enumerate(zip(s,t[bounds[0]:bounds[1]])):
        x,y =item
        if x!=y:
            ans.append(i+1)
            
    helper.print_arr(ans)