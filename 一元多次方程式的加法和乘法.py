# 定義 p 和 q 的兩個多項式
p="2*X^5 + 3*X^3 + 2*X^1 + 5"
q="2*X^3 + 3*X^1 + 6"
# 列印 p 和 q
print(f"p={p}")
print(f"q={q}")
# 將 p 和 q 字串分割為項
p1 = p.replace(" ","").split("+")
q1 = q.replace(" ","").split("+")
# 建立一個字典 r 用來儲存多項式中的每個項的係數
r={}
# 處理 p 中的每個項
for p in p1:
    #將項分割為係數和次數
    #例如"2*X^5"分割為[2,5] "5"分割為 [5]
    p=[int(i)for i in p.split("*X^")] 
    if len(p)>1:
        #如果項中包含次數,則將係數添加到字典r中
        if p[1] in r:
            r[p[1]] += int(p[0])
        else:
            r[p[1]]=int(p[0])
    else:
        #如果項中不包含次數,則將係數添加到字典 r 中次數為0的項
        if 0 in r:
            r[0]+=p[0]
        else:
            r[0]=p[0]
# 處理 q 中的每個項
for q in q1:
    #將項分割為係數和次數
    #例如"2*X^3"分割為[2,53] "6"分割為 [6]
    q=[int(i)for i in q.split("*X^")]
    if len(q)>1:
         #如果項中包含次數,則將係數添加到字典r中
        if q[1] in r:
            r[q[1]]+=int(q[0])
        else:
            r[q[1]]=int(q[0])
    else:
        #如果項中不包含次數,則將係數添加到字典 r 中次數為0的項
        if 0 in r:
            r[0]+=q[0]
        else:
            r[0]=q[0]

# 將字典 r 轉換為降幕排序的項
d=[[k,v] for k,v in r.items()]
d.sort()
d.reverse()
# 將項轉換成字串形式
sss=[]
for i in d:
    sss.append(str(i[1])+"*X^"+str(i[0]))
sss="+".join(sss)
# 輸出相加運算結果
print("p+q="+sss[:-4])
# p 和 q 乘法運算
if len(p1[-1])==1:
    p1[-1]=p1[-1]+"*X^0"
if len(q1[-1])==1:
    q1[-1]=q1[-1]+"*X^0"
p1=[i.split("*X^")for i in p1] # [['2', '5'], ['3', '3'], ['2', '1'], ['5', '0']]
q1=[i.split("*X^")for i in q1]
p1=[[int(j)for j in i]for i in p1] # [[2, 5], [3, 3], [2, 1], [5, 0]]
q1=[[int(j)for j in i]for i in q1] #[[2,3],[3,1],[6,0]]
# 將 P 和 Q 的每一項相乘
r1=[]
lp=len(p1) #4
lq=len(q1) #3
for i in range(lp): #0 1 2 3
    for j in range(lq): #0 1 2
        r1.append([p1[i][0]*q1[j][0],p1[i][1]+q1[j][1]])
#將每一項的細數加總,得到最終的多項式
r={}
for i in r1: #[[4, 8], [6, 6], [12, 5], [6, 6], [9, 4], [18, 3], [4, 4], [6, 2], [12, 1], [10, 3], [15, 1], [30, 0]]
    if i[1] in r:
        r[i[1]]+=i[0]
    else:
        r[i[1]]=i[0]
d=[[k,v]for k,v in r.items()]
d.sort()
d.reverse()
sss=[]
for i in d:
    sss.append(str(i[1])+"*X^"+str(i[0]))
sss="+".join(sss)
#輸出乘法運算結果
print("p*q="+sss[:-4])