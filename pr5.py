with open('input/5') as f:
    char_list = list(f.read())

ascii_values = [ord(c) for c in char_list]
# print(ascii_values)

idx = 0 
out  ='1'
while idx < len(ascii_values):
    if abs(ascii_values[idx] - ord(out[-1])) != 32:
        out += chr(ascii_values[idx])
        idx +=1
    else:
        # print(f'out: {out}')
        out = out[:-1]
        # print(f'Truncated out: {out}')
        idx = idx+1

out = out[1:]
print(f'Problem 1: {len(out)}')


# Problem 2:



# for c in range(65,26+65):
#     print(chr(c), chr(c+32))
lens = []
for c in range(65,65+26):
    # print(chr(c), chr(c+32))
    idx = 0 
    out  ='1'  
    while idx < len(ascii_values):
        if(ascii_values[idx] == c or ascii_values[idx] == c+32):
            idx +=1
        elif abs(ascii_values[idx] - ord(out[-1])) != 32:
            out += chr(ascii_values[idx])
            idx +=1
        else:
            # print(f'out: {out}')
            out = out[:-1]
            # print(f'Truncated out: {out}')
            idx = idx+1
    # print(out[1:])
    lens.append(len(out)-1)

print(f'problem 2: {min(lens)}')









