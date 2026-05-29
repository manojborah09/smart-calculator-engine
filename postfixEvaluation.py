def postfixEvaluation(s):

  evaluate = []

  for chr in s:

    if chr == '+':
      a = evaluate.pop()
      b = evaluate.pop()
      evaluate.append(b+a)

    elif chr == '-':
      a = evaluate.pop()
      b = evaluate.pop()
      evaluate.append(b-a)

    elif chr == '*':
      a = evaluate.pop()
      b = evaluate.pop()
      evaluate.append(b*a)

    elif chr == '/':
      a = evaluate.pop()
      b = evaluate.pop()
      evaluate.append(float(b)/a)

    else:
      evaluate.append(float(chr))

  return evaluate[-1]

  

    