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

mx = 10**5+5000

is_prime = [1 for _ in range(mx+1)]
is_prime[0] = 0
is_prime[1] = 0
for x in range(mx+1):
    if is_prime[x]:
        for y in range(x*x,mx+1,x):
            is_prime[y] = 0

primes = [i for i,x in enumerate(is_prime) if x]
ans = [primes[i]*primes[i+1] for i in range(len(primes)-1)]

t = helper.read_int()
for _ in range(t):
    n = helper.read_int()
    helper.print_arr(ans[:n])