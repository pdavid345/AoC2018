with open('input/1') as f:
   dat = [int(i) for i in f.read().split('\n')]

# part 1
print(sum(dat))

#  part 2
freqs = [0]
freq = 0

isFound = False
while(not isFound):
    for i in dat:
        freq = freq + i
        if(freq in freqs):
            print('FOUND: ',freq)
            isFound = True
        freqs.append(freq)

