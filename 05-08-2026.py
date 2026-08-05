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
    a = helper.read_ints()
    edges = {}
    for i in range(n):
        edges[i] = []
    for i in range(n):
        if i-x >= 0:
            edges[i].append(i-x)
            edges[i-x].append(i)
        if x!=y and i-y >= 0:
            edges[i].append(i-y)
            edges[i-y].append(i)
    
    vis = [0 for _ in range(n)]
    def bfs(node,comp):
        q = [node]
        idx = 0
        while idx < len(q):
            k = q[idx]
            idx+=1
            if vis[k]:
                continue
            vis[k] = 1
            comp.append(k)
            for w in edges[k]:
                q.append(w)
    ans = "YES"
    for i in range(n):
        if vis[i]:
            continue
        comp = []
        bfs(i,comp)
        values = [a[j] for j in comp]
        values.sort()
        comp.sort()
        for j,v in zip(comp,values):
            if j+1!=v:
                ans="NO"
                break
        if ans=="NO":
            break
    print(ans)
