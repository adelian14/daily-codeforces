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
    def is_pal(mnt):
        if mnt==24*60:
            return True
        h = mnt//60
        m = mnt%60
        s = ''
        if h < 10:
            s+='0'
        s+=str(h)
        if m < 10:
            s+='0'
        s+=str(m)
        return s==s[::-1]
    s = helper.read_line()
    h = int(s[:2])
    m = int(s[3:])
    m+=h*60
    ans = 0
    while not is_pal(m):
        m+=1
        ans+=1
    print(ans)
    
    