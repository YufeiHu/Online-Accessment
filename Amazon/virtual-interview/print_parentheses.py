def print_parentheses(P):
    stack = list()
    for p in P:
        if stack and stack[-1] == '(' and p == ')':
            stack.pop()
            print('    ' * len(stack) + p)
        else:
            stack.append(p)
            print('    ' * (len(stack) - 1) + p)

print_parentheses('(()((())()))')