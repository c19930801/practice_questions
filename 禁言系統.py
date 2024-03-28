prohibit=["習","近","平","傻"]

inp=input("請輸入一段文字:")
result=""
for x in inp:
    if x not in prohibit:
        result=result+x
    else:
        result=result+"*"
print(result)