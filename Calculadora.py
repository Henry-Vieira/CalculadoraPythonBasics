""" Calculadora com while """


start = True
while start:
  n1 = input("Digite o primeiro número: ")
  n2 = input("Digite o segundo número: ")
  operadores = input("Digite o operador +-*/: ")

  numeros_validos = None

  try:
    n1 = float(n1)
    n2 = float(n2)
    numeros_validos = True


  except:
    numeros_validos = None
  
  if numeros_validos is None:
    print("Um ou ambos os números digitados não são validos, tente novamente!")
    start = True

  operadores_permitidos = '+-*/'

  if operadores not in operadores_permitidos:
    print("Operador inválido!")
  if len(operadores) > 1:
    print("Digite apenas um operador!")
    start = True

  
  if operadores == '+':
    resultado = n1 + n2
  
  elif operadores == '-':
    resultado = n1 - n2
  
  elif operadores == '*':
    resultado = n1 * n2
  
  elif operadores == '/':
    resultado = n1 / n2

  print(f"O resultado da operação desejada é {resultado}")

  sair = input("Deseja sair? [s]im: ").lower().startswith('s')

  if sair == True:
    start = False

