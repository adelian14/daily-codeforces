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
    s = helper.read_line()
    j = n-1
    i = 0
    ans = "YES"
    def get_chars(k):
        if k=='a':
            return 'b'
        if k=='z':
            return 'y'
        return ''.join([chr(ord(k)+1),chr(ord(k)-1)])        
    while i < j:
        x,y = s[i],s[j]
        a,b = get_chars(x),get_chars(y)
        k = set()
        for c in a+b:
            k.add(c)
        if len(k)==len(a)+len(b):
            ans = "NO"
            break
        i+=1
        j-=1
    print(ans)