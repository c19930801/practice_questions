def is_balanced(equation):
    stack=[]
    for ch in equation: 
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":  
            right_ch = ch
            if not stack:
                return False   
            left_ch = stack.pop()
            if left_ch== "(" and right_ch !=")":
                return False
            if left_ch== "[" and right_ch !="]":
                return False
            if left_ch== "{" and right_ch !="}":
                return False
    if stack:
        return False
    return True

print(is_balanced(""))
print(is_balanced("{[]}"))
print(is_balanced("{[]()}"))
print(is_balanced("){[]()"))
print(is_balanced("({})"))

