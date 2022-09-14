from nn import cal_heart
try:
    a=float(input('enter num a='))
    b=float(input('enter num b= '))
    c=input('enter operator= ')

    r=cal_heart.oper(a,b,c)

    print(r)
except:
    print('enter numbers as a&b')