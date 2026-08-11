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

ops = [
    [[0,1],[1,2],[1,2],[0,2]],
    [[1,2],[0,1],[0,1],[0,2]],
    [[1,2],[1,2],[0,2]],
    [[0,1],[0,1],[0,2]]
]

t = helper.read_int()
for _ in range(t):
    n = helper.read_int()
    a = helper.read_ints()
    if n==1 or n >= 4:
        print(n*max(a))
        continue
    if n==2:
        print(max(sum(a),2*abs(a[0]-a[1])))
        continue
    def solve(i,j,arr):
        diff = abs(arr[j]-arr[i])
        for k in range(i,j+1):
            arr[k] = diff
        return arr
    
    ans = sum(a)
    for arr in ops:
        temp = [x for x in a]
        for i,j in arr:
            temp = solve(i,j,temp)
        ans = max(ans,sum(temp))
    print(ans)