def tokenizer(equation):
  # this function separate the string using stack/list eg: '21+3*7' into ['21','+','3','*','7']

  output = []
  nums = ''
  operators = '+-*/()'

  for i in range(len(equation)):

    chr = equation[i]

    if chr.isspace():
      continue

    elif chr == '-' and (i == 0 or equation[i-1] in operators):
      nums = nums + chr

    elif chr.isdigit() or chr == '.':
      nums = nums + chr
      
    else:

      if nums:
        output.append(nums)
        nums = ''

      output.append(chr)

  if nums:
    output.append(nums)

  return output
