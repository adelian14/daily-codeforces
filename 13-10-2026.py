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
    n,a,b = helper.read_ints()
    arr = helper.read_ints()
    ans = 0
    for i in range(n):
        j = n-i-1
        if arr[i] < 2:
            if arr[j] < 2 and arr[i]!=arr[j]:
                ans = -1
                break
            continue
        if i==j:
            ans+=min(a,b)
        else:
            if arr[j]==0:
                ans+=a
                arr[i] = arr[j]
            elif arr[j]==1:
                ans+=b
                arr[i] = arr[j]
            else:
                ans+=min(a,b)*2
                arr[i] = 1
                arr[j] = 1
    print(ans)
        
    
    
    