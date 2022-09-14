n=1
g=0
c=1
while g<3:
    x=int(input('enter no:- '))
    g=g+1
    if x==n:
        print('correct guess')
        c=1
       # exit()
        break
    elif g==3 and x!=n:
        print('uve run out of turns')
        print('no was '+str(n))
    else:
        print('try again')
        c=0

if c==1:
    print('congrulations')
else:
    print('u lost')