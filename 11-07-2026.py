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
    cnt = [0,0,0,0]
    idx = n
    for i,x in enumerate(a):
        cnt[x]+=1
        if cnt[1] >= cnt[2]+cnt[3]:
            j = i+1
            while j < n-2 and a[j]==3:
                if cnt[1] >= cnt[2]+cnt[3]+1:
                    cnt[3]+=1
                    j+=1
                else:
                    break
                    
            idx = j
            break
    if idx > n-1:
        print("NO")
        continue
    
    cnt = [0,0,0,0]
    ans = "NO"
    for i in range(idx,n):
        cnt[a[i]]+=1
        if cnt[1]+cnt[2] >= cnt[3]:
             if i < n-1:
                 ans = "YES"
                 break
    print(ans)