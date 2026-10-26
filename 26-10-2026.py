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
    a = [[-1 for _ in range(n)] for _ in range(n)]
    x,y = n//2,n//2
    if n%2==0:
        x-=1
        y-=1
    dirs = [[0,1],[1,0],[0,-1],[-1,0]]
    val = 0
    idx = 3
    while val < n*n:
        a[x][y] = val
        val+=1
        nxt = (idx + 1) % 4
        dx,dy = dirs[nxt]
        nx = x+dx
        ny = y+dy
        if min(nx,ny) < 0 or max(nx,ny)==n or a[nx][ny] > -1:
            x+=dirs[idx][0]
            y+=dirs[idx][1]
        else:
            x=nx
            y=ny
            idx = nxt
    for r in a:
        helper.print_arr(r)
        