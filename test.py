def tokenizer(s):

  stack = []
  nums = ''
  operators = '+-*/^()'

  for i in range(len(s)):

    chr = s[i]

    if chr.isspace():
      continue

    elif chr == '-' and (i==0 or s[i-1] in operators):
      nums = nums + chr

    elif chr.isdigit() or chr == '.':
      nums = nums + chr

    else:
      if nums:
        stack.append(nums)
        nums = ''

      stack.append(chr)

  if nums:
    stack.append(nums)

  return stack

s = input("Enter the equation : ")
print(tokenizer(s))