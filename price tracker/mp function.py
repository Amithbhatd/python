def hm(s):
    nm = 0
    nnm = ''
    for x in s:
        if (x.get('m') > nm):
            nm = x.get('m')
            nnm = x.get('n')
    print(f'highest s={nm} and name={nnm}')
def hp(s):
    np =0
    nnp = ''
    for x in s:
        if (x.get('p') > np):
            np = x.get('p')
            nnp = x.get('n')
    print(f'highest s={np} and name={nnp}')
def hs(s):
    ns =0
    nns = ''
    for x in s:
        if (x.get('s') > ns):
            ns = x.get('s')
            nns = x.get('n')
    print(f'highest s={ns} and name={nns}')
s1={
    'm': 100,
    's': 50,
    'p': 35,
    'n': 'aaa'
}
s2={
    'm': 10,
    's': 40,
    'p': 45,
    'n': 'bbb'
}
s3={
    'm': 69,
    's': 55,
    'p': 30,
    'n': 'ccc'
}
s=[s1,s2,s3]
hm(s)
hp(s)
hs(s)
