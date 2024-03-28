""" josephus問題是著名的數學問題,有N個人站成一個圓圈，從第一個人開始屬m數,報到m的人出圈,剩下的人繼續報數,
重複此過程,直到所有人都出圈為止,問最後出圈的人在原先圓圈的位置是多少? """
from queue import Queue # 引入Queue類別模組
def josephus(n,m):
    q=Queue() #建立一個 Queue 物件
    for i in range(1,n+1): #將編號 1~15 的人放入 Queue 
        q.put(i) #放入
    while q.qsize()>1: #只要還有人在 Queue 裡面就繼續
        for i in range(m-1): #將Queue 的前4格放到Queue的未尾 0 1 2 3
            q.put(q.get())
        q.get() #第4個人出列 #取出
    return q.get()
    
n=15 #總人數
m=4 #每次報數的數字
#最後執行 josephus 涵式算出答案
print(f"最後出圈的是:{josephus(n,m)}")