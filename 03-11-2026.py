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

n = helper.read_int()
s = helper.read_line()
t = helper.read_int()
p = [[0 for _ in range(26)] for _ in range(n)]
for i in range(n):
    if i:
        for j in range(26):
            p[i][j] = p[i-1][j]
    p[i][ord(s[i])-ord('a')]+=1
for _ in range(t):
    k = helper.read_line()
    q = [0 for _ in range(26)]
    for x in k:
        q[ord(x)-ord('a')]+=1
    l = 0
    r = n-1
    while l <= r:
        mid = (l+r)//2
        flag = 1
        for i in range(26):
            if p[mid][i] < q[i]:
                flag = 0
                break
        if flag:
            r = mid-1
        else:
            l = mid+1
    print(l+1)
        