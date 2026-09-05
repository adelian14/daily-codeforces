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

tests = helper.read_int()
for _ in range(tests):
    n,q = helper.read_ints()
    s = helper.read_line()
    t = helper.read_line()
    pre = [[0 for _ in range(n+1)] for _ in range(4)]
    for i in range(1,n+1):
        x,y = s[i-1],t[i-1]
        idx = 0
        if x=='1':
            idx = 2
        if y=='1':
            idx += 1
        pre[0][i] = pre[0][i - 1]
        pre[1][i] = pre[1][i - 1]
        pre[2][i] = pre[2][i - 1]
        pre[3][i] = pre[3][i - 1]
        pre[idx][i]+=1
    for _ in range(q):
        l,r = helper.read_ints()
        a = pre[0][r] - pre[0][l - 1]
        b = pre[1][r] - pre[1][l - 1]
        c = pre[2][r] - pre[2][l - 1]
        d = pre[3][r] - pre[3][l - 1]
        if abs(b-c) <= a+d:
            print("YES")
        else:
            print("NO")