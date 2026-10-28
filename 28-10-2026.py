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
    n,k = helper.read_ints()
    a = helper.read_ints()
    b = helper.read_ints()
    p = [x for x in b if x > -1]
    p.sort()
    flag = 0
    for i in range(1,len(p)):
        if p[i]==p[i-1]:
            flag = 1
            break
    if flag:
        print("NO")
        continue
    if n==k:
        print("YES")
        continue
    cnt = n-k
    flag = 1
    for i in range(cnt):
        j = n-i-1
        if (a[i]!=b[i] and b[i]!=-1) or (a[j]!=b[j] and b[j]!=-1):
            flag = 0
            break
        if b[i]==-1:
            b[i]=a[i]
        if b[j]==-1:
            b[j]=a[j]
    p = [x for x in b if x > -1]
    p.sort()
    for i in range(1,len(p)):
        if p[i]==p[i-1]:
            flag = 0
            break
    if flag:
        print("YES")
    else:
        print("NO")