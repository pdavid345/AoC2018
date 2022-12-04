import regex as re

with open('input/3') as f:
   dat = [[int(i) for i in j] for j in re.findall('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)',f.read())]

# print(dat)
xlim = max([i[1]+i[3]-1 for i in dat])
ylim = max([i[2]+i[4]-1 for i in dat])
print(xlim, ylim)



