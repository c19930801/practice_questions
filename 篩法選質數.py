def arr(n):
    p=[2,3,5,7]
    for k in range(2):
        d=list(range(2,n+1))
        for i in p:
            for j in d:
                if j%i==0:
                    d.remove(j)
    return p+d
print(arr(100))

