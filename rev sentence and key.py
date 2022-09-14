txt='this is a test case sentence'
def aa(ps):
    n=0
    for d in ps:    #d is the index of the words hence no of words counted through indexing
        n=n+1
    return n
sp = txt.split()
print(sp)
sp.reverse()
ps= sp
print(ps)
ab=aa(ps)
print(f"the total num of words= {ab}")
x=input('key1 ;')
y=input('key2 ;')
print(ps[int(x):int(y)])