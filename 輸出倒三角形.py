floor=input("請輸入你想要幾層的倒三角形:")
max=(int(floor)*2)-1
for x in range(0,int(floor)):
    print(" "*x,"*"*(max-2*x)," "*x)