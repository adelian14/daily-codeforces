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
    p = []
    for x in a:
        if len(p) < 2 or x!=p[-1] or x!=p[-2]:
            p.append(x)
    done = 0
    for i in range(max(0,len(p)-3)):
        if p[i]==p[i+1] and p[i+2]==p[i+3]:
            p[i+1],p[i+2] = p[i+2],p[i+1]
            done = True
            break
    
    if not done:
        for i in range(max(0,len(p)-4)):
            if p[i]==p[i+1] and p[i+3]==p[i+4] and p[i]!=p[i+3]:
                p[i+1],p[i+3] = p[i+3],p[i+1]
                p[i+2] = -1
                done = True
                break
    
    if not done:
        for i in range(2,len(p)):
            if p[i]==p[i-1]:
                if i-3 < 0 or p[i-3]!=p[i]:
                    p[i-1],p[i-2]=p[i-2],p[i-1]
                    done = True
                    break
    if not done:
        for i in range(max(0,len(p)-2)):
            if p[i]==p[i+1]:
                if i+3 >= len(p) or p[i+3]!=p[i]:
                    p[i+1],p[i+2] = p[i+2],p[i+1]
                    done = True
                    break
    
    ans = []
    for x in p:
        if x==-1:
            continue
        if len(ans) and x==ans[-1]:
            continue
        ans.append(x)
    print(len(ans))
    