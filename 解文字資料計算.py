a="""
第01關:變數與計算
共12題
完成12題

第02關:變數與類別
共16題
完成16題

第03關:運算子
共2題
完成2題

第04關:分支
共16題
完成16題
"""
q=[i[:5]for i in a.split("\n") if "第" in i]
p=[i[:5]for i in a.split("\n") if "完成" in i]
for i in range(len(p)):
    print(q[i],p[i])
a=",".join(p).replace("完成","").replace("題","")
a=[int(i)for i in a.split(",")]
print(f"總解題數:{sum(a)}題")
