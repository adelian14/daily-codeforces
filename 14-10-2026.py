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
    a1 = helper.read_int()
    a2 = helper.read_int()
    k1 = helper.read_int()
    k2 = helper.read_int()
    n = helper.read_int()
    if k1 < k2:
        k1,k2 = k2,k1
        a1,a2 = a2,a1
    def get_mx(a,b,p,q,n):
        ans = 0
        while b:
            if q > n:
                break
            ans+=1
            b-=1
            n-=q
        while a:
            if p > n:
                break
            ans+=1
            a-=1
            n-=p
        return ans
    def get_mn(a,b,p,q,n):
        n-=(p-1)*a
        n-=(q-1)*b
        return max(n,0)
    mn = get_mn(a1,a2,k1,k2,n)
    mx = get_mx(a1,a2,k1,k2,n)
    print(mn,mx)