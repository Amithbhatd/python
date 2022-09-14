def oper(a,b,c):
    if (c == '+'):
        c=add(a, b)
        return c
    elif (c == '-'):
        c=sub(a,b)
        return c
    elif(c=='*'):
        c=mul(a,b)
        return c
    elif(c=='/'):
        c=div(a,b)
        return c
    elif(c=='power'):
        c=power(a,b)
        return c
    else:
        return 'invalid operator'
def add(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b
    return c
def mul(a,b):
    c=a*b
    return c
def div(a,b):
    c=a/b
    return c
def power(a,b):
    c=a**b
    return c