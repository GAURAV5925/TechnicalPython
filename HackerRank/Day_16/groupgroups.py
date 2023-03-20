import re

s = input()

m = re.search(r'([0-9a-zA-Z])\1',s)

if m:
    print(m.groups()[0])
    #Here the group(0) will not run and give the nonetype
else:
    print(-1)
