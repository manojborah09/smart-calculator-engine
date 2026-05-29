from tokenizer import tokenizer
from infixToPostfix import infixToPostfix
from postfixEvaluation import postfixEvaluation

def main():

  print("==========\nCalculator\n==========")
  print("To Exit the Calulator type 'EXIT'")

  while True :

    expression = input('Enter the Expression to solve : ')

    if expression.upper() == 'EXIT':
      break

    token = tokenizer(expression)
    infix = infixToPostfix(token)
    output = postfixEvaluation(infix)

    print(f'{output}')
    
main()