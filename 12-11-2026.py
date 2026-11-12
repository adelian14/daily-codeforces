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
    a,b = helper.read_ints()
    nums = [6,2,5,5,4,5,6,3,7,6]
    ans = 0
    k = 0
    for i in range(1,1000):
        x = i
        while x:
            k += nums[x%10]
            x//=10
        if i < 10:
            k+=12
        elif i < 100:
            k+=6
    while a <= b:
        x = a
        val = 0
        while x:
            val+=nums[x%10]
            x//=10
        ans += val
        if a%1000==0 and a+999 <= b:
            val-=18
            ans+=val*999+k
            a+=999
        a+=1
            
    print(ans)
    
    