import random
ans=[]
m=0
print("遊戲規則:隨機產生4個不重復的0-9數字,若數字正確且位子相同得到1A,若數字正確位子不同得到1B")
print("例如:p=1234,q=4321,因為1和3是不同位置上的數字,所以B=2:而4是相同位置上的數字,所以A=1,算出1A2B")
while m <4:
    ar=random.randint(0,9)
    if ar not in ans:
        ans.append(ar)
        m+=1
print("請輸入4個數字:")
while True:
    inp=input()
    answ=[]
    for i in inp:
        answ.append(i)
    print(f"你輸入的是{answ}")
    A=0
    B=0
    for i in range(4):
        if int(answ[i])==int(ans[i]):
            A+=1
        if int(answ[i])in ans:
            B+=1
    if A!=4:
        print(f"{A}A{B}B")
        print("這不是正確答案,請再輸入一次:")
    if A==4:
        break
print("恭喜你答對正確答案:",ans)
