# Python fucntion to evaluate a string expression: Alternative to eval function

def eval2(s):
    k = s.split('+')
    p = []
    q = []
    r = 0
    t = 0
    for j in k:
        if '-' in j:
            r = int(j.split('-')[0]) + r
            for i in j.split('-')[1:]:
                q.append(int(i))

        else:
            p.append(int(j))
        
    return(sum(p) - sum(q) + r)
                     


x = "1+2-3+4"

y = "1+2-3-4+5-6-7"

print(eval2(x))
