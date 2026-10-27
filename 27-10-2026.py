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
    a.sort()
    a = a[::-1]
    ans = 0
    for i in range(1,n):
        for j in range(i+1,n):
            upper = a[i]+a[j]-1
            lower = a[0]-a[i]-a[j]+1
            if lower > upper:
                continue
            l = 0
            r = i-1
            mn = -1
            mx = -1
            while l <= r:
                mid = (l+r)//2
                if a[mid] >= lower:
                    l = mid+1
                    mn = mid
                else:
                    r = mid-1
            if mn==-1:
                continue
            l = 0
            r = i-1
            while l <= r:
                mid=(l+r)//2
                if a[mid] <= upper:
                    r = mid-1
                    mx = mid
                else:
                    l = mid+1
            if mx==-1:
                continue
            ans += (mn-mx)+1
    print(ans)
    
    