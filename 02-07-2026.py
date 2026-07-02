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
    exist = [0 for _ in range(n+1)]
    for x in a:
        exist[x] = 1
    will_be_added = [i for i,x in enumerate(exist) if not x and i]
    m = len(will_be_added)
    j = m-1
    for i in range(n):
        if not a[i]:
            a[i] = will_be_added[j]
            j-=1
    first = -1
    last = -1
    for i,x in enumerate(a):
        if i+1!=x:
            first = i
            break
    for i in range(n-1,-1,-1):
        if i+1!=a[i]:
            last = i
            break
    if first == -1:
        print(0)
        continue
    print(last-first+1)
    
    