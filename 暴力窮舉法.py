"""邏輯思考題目
有五間房屋排成一列，所有的房屋外表顏色不一樣
所有的屋主都來自不同的國家,養不同的寵物，喝不同的飲料，抽不同的香菸
英國人住在紅色房屋，瑞典人養了一隻狗，丹麥人喝茶
綠色的房子在白色的房子左邊、綠色房屋的屋主喝咖啡、抽Pall Mall香菸的屋主養鳥、黃色屋主抽Dunhil
位於最中間的屋主喝牛奶，挪威人住在第一間房屋裡，抽Blend的人住在養貓人家隔壁、養馬的屋主隔壁住抽Dunhil的人家
抽Blue Master的屋主他喝啤酒，德國人抽Price
挪威人住在藍色房子隔壁、只喝開水的人家住在抽Blend的隔壁
問題:請問誰養斑馬?
"""
countrys=["丹麥","英國","瑞典","德國","挪威"]
animals=["狗","斑馬","貓","鳥","馬"]
drinks=["茶","啤酒","咖啡","牛奶","水"]
houses=["紅","黃","白","綠","藍"]
smokes=["Price","Blend","Pall Mall","Dunhil","Blue Master"]
a=[]
count=0
for country in countrys:
    for animal in animals:
        for drink in drinks:
            for house in houses:
                for smoke in smokes:
                    #問題:請問誰養斑馬?
                    if animal !="斑馬":continue #剔除所有沒有養斑馬的答案
                    # 1 英國人住在紅色房屋
                    if house =="紅"and country!="英國":continue
                    if house !="紅"and country=="英國":continue
                    # 2 瑞典人養了一隻狗
                    if country!="瑞典"and animal=="狗":continue
                    if country=="瑞典"and animal!="狗":continue
                    # 3 丹麥人喝茶
                    if country!="丹麥"and drink=="茶":continue
                    if country=="丹麥"and drink!="茶":continue
                    # 4 綠色的房子在白色的房子左邊
                    if house =="綠"and (houses.index("白")-houses.index("綠")) !=1:continue #.index此方法傳回查找物件的索引位置 綠在白左 故索引位子相減為1
                    if house =="白"and (houses.index("白")-houses.index("綠")) !=1:continue
                    # 5 綠色房屋的屋主喝咖啡
                    if house!="綠"and drink=="咖啡":continue
                    if house=="綠"and drink!="咖啡":continue
                    # 6 抽Pall Mall香菸的屋主養鳥
                    if smoke!="Pall Mall"and animal=="鳥":continue
                    if smoke=="Pall Mall"and animal!="鳥":continue
                    # 7 黃色屋主抽Dunhil
                    if smoke!="Dunhil" and house =="黃":continue
                    if smoke=="Dunhil" and house !="黃":continue
                    # 8 位於最中間的屋主喝牛奶
                    if drink=="牛奶"and drink.index(drink)!=2:continue
                    # 9 挪威人住在第一間房屋裡
                    if country=="挪威"and countrys.index("挪威")!=0:continue
                    # 10 抽Blend的人住在養貓人家隔壁
                    if smoke=="Blend"and abs(animals.index(animal)-animals.index("貓"))!=1:continue
                    # 11 養馬的屋主隔壁住抽Dunhil的人家
                    if animal=="馬"and abs(smokes.index(smoke)-smokes.index("Dunhil"))!=1:continue
                    # 12 抽Blue Master的屋主他喝啤酒
                    if smoke=="Blue Master"and drink!="啤酒":continue
                    if smoke!="Blue Master"and drink=="啤酒":continue
                    # 13 德國人抽Price
                    if country!="德國"and smoke=="Price":continue
                    if country=="德國"and smoke!="Price":continue
                    # 14 挪威人住在藍色房子隔壁
                    if country=="挪威" and abs(houses.index(house)-houses.index("藍色"))!=1:continue
                    # 15 只喝開水的人家住在抽Blend的隔壁
                    if drink=="水"and abs(smokes.index(smoke)-smokes.index("Blend"))!=1:continue
                    count+=1
                    t=str(count)+"種可能:"+country+"人,養"+animal+"喝著"+drink+"住著"+house+"的房子,抽著"+smoke+"牌子的菸"
                    a.append(t)
for i in a:
    print(i)