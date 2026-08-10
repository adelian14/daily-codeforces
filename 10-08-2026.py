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
    n,x,y = helper.read_ints()
    s = helper.read_line()
    cnt = s.count('A')
    def solve(num,k):
        used = 0
        ans = 0
        for c in s:
            if c=='I':
                if num:
                    ans+=1
                    num-=1
                    if y-1:
                        used+=(y-1)
            elif c=="E":
                if used:
                    ans+=1
                    used-=1
            else:
                if num and k:
                    k-=1
                    ans+=1
                    num-=1
                    if y-1:
                        used+=(y-1)
                elif used:
                    ans+=1
                    used-=1
        return ans

    ans = 0
    for k in range(0,cnt+1):
        ans = max(ans,solve(x,k))
    print(ans)