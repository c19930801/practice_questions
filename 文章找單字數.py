a="A long time ago, there was a huge apple tree. A little boy loved to come and lay around it every day. He climbed to the tree top, ate the apples, took a nap under the shadow… He loved the tree and the tree loved to play with him.Time went by… the little boy had grown up and he no longer played around the tree every day. One day, the boy came back to the tree and he looked sad. “Come and play with me,” the tree asked the boy. “I am no longer a kid, I don't play around trees anymore.” The boy replied, “I want toys. I need money to buy them.” “Sorry, but I don't have money…but you can pick all my apples and sell them. So, you will have money.” The boy was so excited. He grabbed all the apples on the tree and left happily. The boy never came back after he picked the apples. The tree was sad."
b =[i for i in a.split() if i>="A" and i<"z"] #用迴圈的方式把字串打散成列表 並且用if去除 A-Z字母 以外的符號
c=set(b) #轉換為集合,特性不重複
for i in c:
    print(f"{i}出現了:{b.count(i)}次")
print(f"文章中總共出現了{len(c)}個單字")