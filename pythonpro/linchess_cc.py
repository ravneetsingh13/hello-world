T = int(input())
for _ in range(T):
    N, K = [int(i) for i in input().split()]
    P = list(map(int,input().split()))
    R = list()
    for i in P:
        s=i
        m=0
        while(i<K):
            i+=s
            if(i>K):
                m=0
                R.append(m)
                break
            m+=1
            if(i==K):
                R.append(m)
                break
        else:
            R.append(m)
    print(R)
    l = 0
    for i in range(len(R)):
        if(R[i]>0):
            l=R[i]
            ind = i
            break
    if l==0:
        print(-1)
    else:
        for i in range(len(R)):
            if(R[i]<l and R[i]>0):
                l=R[i]
                ind = i
        print(P[ind])
