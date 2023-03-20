import re

s = input()
ss = input()

p = re.compile(ss)
m = p.search(s)
if not m:
    print("(-1, -1)")
else:
    while m:
        print("({0}, {1})".format(m.start(),m.end()-1))
        m = p.search(s,m.start() + 1)
