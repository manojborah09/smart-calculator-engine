
def isNumber(x):

  try:
    float(x)
    return True
  
  except:
    return False


def infixToPostfix(s):
  # This function convert infix to postfix (Reverse Polish Notation) i.e. 2*9+6 -> 29*6+

  precedence = {
    '^': 4,
    '*': 3,
    '/': 3,
    '+': 2,
    '-': 2,
    '(': 1
  }

  main_output = []
  stack = []

  for chr in s:

    if chr == '(':
      stack.append(chr)

    elif chr == ')':
      while not stack[-1] == '(':
        main_output.append(stack.pop())
      
      stack.pop()

    elif isNumber(chr):
      main_output.append(chr)

    else:

      while (stack and stack[-1] != '(' and precedence[chr] <= precedence[stack[-1]]):
        main_output.append(stack.pop())

    stack.append(chr)

  while stack:
    main_output.append(stack.pop())

  return main_output


    
  
