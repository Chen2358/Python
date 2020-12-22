from allpairspy import AllPairs

# 子列表类比下拉框

old = [['a', 'b', 'c', 'd'], ['e', 'f', 'g'], ['h', 'i']]
ready = []

for pairs in AllPairs(old[:2]):  # 组合前两个列表
    ready.append(''.join(pairs))

for i in range(2, len(old)):  # 上一步组合的列表再和下一个子列表组合
    new_r = []
    for pairs in AllPairs([ready, old[i]]):
        new_r.append(''.join(pairs))
        ready = new_r

print(ready)
print(len(ready))
