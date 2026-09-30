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
    rows = []
    cols = []
    for _ in range(n):
        rows.append(helper.read_ints())
    for _ in range(m):
        cols.append(helper.read_ints())
    ref_col = None
    for col in cols:
        if not ref_col:
            for x in col:
                if x == rows[0][0]:
                    ref_col = [k for k in col]
                    break
    row_index = [[x[0],i] for i,x in enumerate(rows)]
    for x in ref_col:
        for y,idx in row_index:
            if x==y:
                helper.print_arr(rows[idx])
                break
    
    
    