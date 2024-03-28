def dec_10_18(n): #10進位轉18進位函式
    rr="0123456789ABCDEFGH" # rr是一個用來儲存18進位每個位數對應的字元的字串
    if n==0: #如果 n 為0,直接回傳字串"0"
        return "0"
    digit18=[] #建立一個空的串列digit18 用來儲存轉換後的數字
    while n>0:
        r= n%18 #取得n除以18的餘數
        digit18.append(rr[r]) #將餘數對應的字元加到 digit18 串列中
        n=n//18 #將n除以18
    digit18.reverse() #list.reverse() :將列表中的項目順序前後反過來
    digit18="".join(digit18) #"指定字串".join(要連接的字串) #:使用指定字串將串列連接起來
    return digit18 #回傳最後的到的18進位數字
for i in range(20):
    digit18=dec_10_18(i)
    print(f"{i} : {digit18}")
