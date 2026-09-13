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
    if k < n or k >= 2*n:
        print(-1)
        continue
    diff = k-n+1
    a = [[0 for _ in range(n)] for _ in range(n)]
    a[0][0] = 1
    val = 2
    for i in range(1,diff):
        a[i][0] = val
        val+=1
        a[0][i] = val
        val+=1
    for i in range(diff,n):
        if not a[i][i]:
            a[i][i] = val
            val+=1
    for i in range(n):
        for j in range(n):
            if not a[i][j]:
                a[i][j] = val
                val+=1
                
    for r in a:
        helper.print_arr(r)