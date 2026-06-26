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
    mx = [x for x in a]
    ans = 0
    for i in range(1,n):
        mx[i] = max(mx[i],mx[i-1])
    for i in range(n-1,-1,-1):
        if i&1:
            if i+1 < n:
                if a[i] <= max(a[i-1],a[i+1]):
                    a[i]=mx[i]
                    if a[i+1] >= a[i]:
                        val = a[i]-1
                        ans+=(a[i+1]-val)
            else:
                if a[i] <= a[i-1]:
                    a[i]=mx[i]
        else:
            if i+1 < n:
                if a[i]==a[i+1]:
                    ans+=1
                    a[i]-=1
                    
    print(ans)