# 樂透開獎，模擬10000次，統計得獎狀況，考慮特別號
import random
def Lotto(frequency):
    ac=[]
    for j in range(frequency):
        a=[]
        for i in range(100):
            t=random.randint(1,49)
            if t not in a:
                a.append(t)
        outN=a[:6]
        # 取第七個數字a[6]為特別號
        sNum=a[6]
        outN.sort() #.sort()排序

        c=0
        g1=[11,12,23,24,35,36]
        for i in g1:
        # 考慮特別號
            if i in outN:
                c=c+2
            if i==sNum:
                c=c+1
            if c==5:
                c=6
            ac.append(c)
    return ac
# 執行程式
a=1000
b=Lotto(a)
for i in range(1,8):
    print(f"執行{a}次後,總共中{i}獎 :{b.count(13-i)}次")
  