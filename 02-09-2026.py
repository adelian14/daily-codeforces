import os
import sys

class TestcaseHelper:
    def __init__(self):
        testcases_path = '_codeforces_testcases.txt'
        if os.path.exists(testcases_path):
            with open(testcases_path, 'rb') as f:
                self.data = f.read().split()
        else:
            self.data = sys.stdin.buffer.read().split()
        self.current_index = 0
        self.output = []

    def read_int(self):
        x = int(self.data[self.current_index])
        self.current_index += 1
        return x

    def read_ints(self, n):
        i = self.current_index
        j = i + n
        arr = list(map(int, self.data[i:j]))
        self.current_index = j
        return arr

    def print_arr(self, arr):
        self.output.append(' '.join(map(str, arr)))

    def print_val(self, x):
        self.output.append(str(x))

    def flush(self):
        sys.stdout.write('\n'.join(self.output))

helper = TestcaseHelper()

t = helper.read_int()

for _ in range(t):
    n = helper.read_int()
    b = helper.read_ints(n)
    a = [x for x in b]
    a.sort()

    if a[0] != 0:
        helper.print_val(-1)
        continue
    
    vals = {}
    last = 0
    valid = True
    i = 0
    while i < n:
        cur = a[i]
        j = i + 1
        while j < n and a[j] == cur:
            j += 1
        cnt = j - i

        if j == n:
            vals[cur] = last + 1
            break

        nxt = a[j]
        diff = nxt - cur
        if diff % cnt != 0:
            valid = False
            break

        x = diff // cnt

        if x <= last:
            valid = False
            break

        vals[cur] = x
        last = x
        i = j

    if not valid:
        helper.print_val(-1)
        continue

    ans = [vals[x] for x in b]
    helper.print_arr(ans)

helper.flush()