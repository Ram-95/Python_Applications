#Calculator - A Command Line Application that does basic Arithmetic Opertions.(Divison, Multiplication, Addition, Subtraction)

'''Postfix evaluation'''
def postfix_evaluation(st, n):
    '''Evaluates a Postfix Expression and returns the answer(an Integer).'''

    #Operand Stack - Only contains the Operands
    operand_stack = []

    for i in range(n):
        if st[i] not in ('/', '*', '-', '+'):
            operand_stack.append(st[i])
        else:
            a = float(operand_stack.pop())
            b = float(operand_stack.pop())
            if st[i] == '/':
                val = b / a
            elif st[i] == '*':
                val = a * b
            elif st[i] == '+':
                val = a + b
            elif st[i] == '-':
                val = b - a

            operand_stack.append(val)
        #print('OS: {}'.format(operand_stack))

    return operand_stack[-1]



'''Infix to Postfix conversion'''
def infix_to_postfix(s, n):
    '''Converts a given Infix expression to Postfix Expression. Returns the Postfix Expression as a String.'''
    #Operator Stack - Only contains Operators
    stack = []
    #Precedence of Arithmetic Operators
    operator_precedence = {'/' : 4, '*' : 3, '+' : 2, '-' : 1}
    #To store the postfix notation as a list
    res = []

    for i in range(n):
        if s[i] not in operator_precedence:
            if i == 0:
                res.append(s[i])
            else:
                if s[i-1] not in operator_precedence:
                    res[-1] = res[-1] + s[i]
                else:
                    res.append(s[i])

        else:
            if len(stack) == 0:
                stack.append(s[i])
            else:
                if operator_precedence.get(stack[-1]) > operator_precedence.get(s[i]):
                    res.append(stack[-1])
                    stack.pop()
                    stack.append(s[i])
                else:
                    stack.append(s[i])

    #Adding the remaining operators to the result
    while len(stack) != 0:
        res.append(stack[-1])
        stack.pop()
    print(res)
    return postfix_evaluation(res, len(res))




#Driver Code
'''Taking mathematical expression as a String'''
s = input('Expression: ').strip()
print(infix_to_postfix(s, len(s)))


'''
To Do:
---------------
Failing to handle Associativity ----> Left to Right Associativity
Left Most Operation should be evaluated first.
'''
