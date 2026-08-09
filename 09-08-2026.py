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
    n,k = helper.read_ints()
    a = helper.read_ints()
    p = [1]
    for i in range(1,n):
        if a[i]==a[i-1]:
            p[-1]+=1
        else:
            p.append(1)
    p.sort()
    d = 0
    ans = 0
    i = 0
    while i < len(p):
        x = p[i]-1
        y = len(p)-i
        curr = n-d-x*y
        if curr <= k and (k-curr)%y==0:
            ans+=1
        j = i
        while j < len(p) and p[j]==p[i]:
            j+=1
        d+=(j-i)*p[i]
        i = j
    print(ans)