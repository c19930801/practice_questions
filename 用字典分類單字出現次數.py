s="A long time ago, there was a huge apple tree. A little boy loved to come and lay around it every day. He climbed to the tree top, ate the apples, took a nap under the shadow… He loved the tree and the tree loved to play with him.Time went by… the little boy had grown up and he no longer played around the tree every day. One day, the boy came back to the tree and he looked sad. “Come and play with me,” the tree asked the boy. “I am no longer a kid, I don't play around trees anymore.” The boy replied, “I want toys. I need money to buy them.” “Sorry, but I don't have money…but you can pick all my apples and sell them. So, you will have money.” The boy was so excited. He grabbed all the apples on the tree and left happily. The boy never came back after he picked the apples. The tree was sad."

# 宣告一個空字典freq，用來統計個單字出現的次數
freq={}
# 將字串 s 以空格切割成多個單字，使用for 迴圈追蹤這些單字
# 將每個單字轉換成小寫，作為字典的 key ,如果該單字已存在字典中,則其 value 加1,否則 value 初始化為1
for word in s.split():
    freq[word.lower()] =freq.get(word.lower(),0)+1 
# 宣告一個空列表t,用來存放每個單字出現的次數及其單字本身
t=[]
for k,v in freq.items(): #用 items() 將字典轉換為列表 透過 for 迴圈對應到 k 跟 v 中
    t.append([v,k]) # 數字部分在前面 方便等下個列表排序
# 計算總字數,並輸出結果
sum_all=sum(freq.values()) #抓取 freq 中的所有值,並相加
print(f"此文章中總共有{sum_all}個單字")
# 對列表t進行排序,按照出現次數從小排到大排序
t.sort()
#對列表t進行排序,按照出現次數從大排到小排序
t.reverse()
# 宣告計數 c 和 變數 sum10,用來計算前10個出現頻率最高的單字出現的總次數
c=1
sum10=0
for i in t:
    # 逐個列出前10個出現頻率最高的單字及其出現次數
    print(f"單字[{i[1]}]出現了{i[0]}次")
    sum10= sum10 + i[0]
    #每列出一個單字就將計數器 c 加1,如果 c 超過10,就跳出 for迴圈
    c+=1
    if c>10:
        break
# 計算前10個出現頻率最高的單字出現的總次數,以及占總字數比率,並輸出結果
rate =sum10/sum_all*100 #前10字總和除與 全部字數總和
rate =int(rate*10+0.5)/10 #+0.5用意 四捨五入 因為int只抓到整數
print(f"前10個頻率最高的字出現次數:合計{sum10}次")
print(f"前10個頻率最高的字,佔所有字比率:{rate}%")