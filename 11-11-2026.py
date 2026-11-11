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
    n = helper.read_int()
    a = [[0 for _ in range(105)] for _ in range(105)]
    while n:
        x,y,z,w = helper.read_ints()
        a[x][y]+=1
        a[x][w+1]-=1
        a[z+1][y]-=1
        a[z+1][w+1]+=1
        n-=1
ans=0
for i in range(1,101):
    for j in range(1,101):
        a[i][j]+=a[i-1][j]+a[i][j-1]-a[i-1][j-1]
        ans+=a[i][j]
print(ans)
    
    