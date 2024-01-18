import sys
input = sys.stdin.readline

sent = []

while True:
    temp = input().rstrip()
    if temp == '.':
        break
    sent.append(temp)

def check(sent):
    stack = []
    for c in sent:
        if c == '[' or c == '(':
            stack.append(c)
        elif c == ']' or c == ')':
            if len(stack) == 0:
                return 'no'
            elif stack[-1] == '[' and c == ']':
                stack.pop()
            elif stack[-1] == '(' and c == ')':
                stack.pop()
            else:
                return 'no'
    
    if len(stack) == 0:
        return 'yes'
    else:
        return 'no'
            
for s in sent:
    print(check(s))