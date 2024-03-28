def is_balanced(s):
    stack=[]
    pDict={"(":")","[":"]","{":"}"}
    for c in s:
        if c in pDict.keys():
            stack.append(c)
        elif c in pDict.values():
            if len(stack)==0 or pDict[stack[-1]]!=c:
                return False
            stack.pop()
    return len(stack)==0
s="{((55688))}"
print(is_balanced(s))  
# s="({{[}})"  
# print(is_balanced(s))