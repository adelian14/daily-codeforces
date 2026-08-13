import os
import random
import sys

class TestcaseHelper:
    def __init__(self):
        self.local_env = True
        self.input_lines = None
        self.current_index = -1
        testcases_path = '__codeforces_testcases.txt'
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
    a = [i+1 for i in range(2*n)]
    random.shuffle(a)
    found = False
    for i in range(2,2*n,2):
        print(f'? {a[i]} {a[i+1]}')
        x = helper.read_int()
        if x:
            print(f'! {a[i]}')
            sys.stdout.flush()
            found = True
            break
    if not found:
        print(f'? {a[0]} {a[2]}')
        sys.stdout.flush()
        x = helper.read_int()
        if x:
            print(f'! {a[0]}')
            sys.stdout.flush()
        else:
            print(f'? {a[0]} {a[3]}')
            sys.stdout.flush()
            x = helper.read_int()
            if x:
                print(f'! {a[0]}')
                sys.stdout.flush()
            else:
                print(f'! {a[1]}')
                sys.stdout.flush()
            