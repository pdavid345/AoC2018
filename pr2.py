with open('input/2') as f:
   dat = f.read().split('\n')

# print(dat)

def counter(s):
    A = [s.count(c) for c in list(set(s))]
    return [A.count(2)>0, A.count(3)>0]

print(sum([counter(l)[0] for l in dat]) * sum([counter(l)[1] for l in dat]))




def solvePr2(dat):
    L = len(dat[0])-1
    for i in dat:
        for j in dat:
            if  (sum([list(i)[k]==list(j)[k] for k in range(L)]) == L - 1):
                s =''
                for k in range(L):
                    if(list(i)[k] == list(j)[k]):
                        s = s+list(i)[k]
                return(s)



print(solvePr2(dat))
