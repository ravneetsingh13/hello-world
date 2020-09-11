t = int(input())
for _ in range(t):
    n = int(input())
    s = input().lower()
    l = [0] * 26
    flag = True
    if(n % 2 != 0):
        print('NO')
    else:
        for ch in s:
            n = ord(ch)
            l[n - 97] += 1
        for i in l:
            if(i % 2 != 0):
                print('NO')
                flag = False
                break
        if(flag):
            print('YES')
