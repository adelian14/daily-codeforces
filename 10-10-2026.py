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

def get_num(x):
    ans = 0
    while x:
        ans += (x%10)**2
        x//=10
    return ans

mp = [0 for _ in range(730)]
for i in range(1,730):
    x = i
    for _ in range(19):
        x = get_num(x)
    mp[i] = x

t = helper.read_int()
for _ in range(t):
    n = helper.read_int()
    a = helper.read_ints()
    ans = 0
    cnt = {}
    for x in a:
        x = mp[get_num(x)]
        if x in cnt:
            ans+=cnt[x]
            cnt[x]+=1
        else:
            cnt[x] = 1
    print(ans)
    
