#This program will sort an integer array based on alphabetiacal english names
import math

def getName(n):
    a = ['zero','one','two','three','four','five','six','seven','eight','nine']
    m = n
    d = 10**int(math.log10(n))
    t = ''
    while(m!=0):
        n = int(m/d)
        m = m % d
        d = int(d/10)
        t += a[n]
    return t


l = [1,22,44,3456,9999]
l.sort(key=getName)
print(l)
