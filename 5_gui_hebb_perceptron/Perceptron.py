def TestesAND(w0, w1, w2, wb, bias, entradas):
  print("Pesos aprendidos: ({}, {}, {})".format(w0, w1, w2))
  contador = 0
  saida = 0
  E = 0
  print("\nSaídas:")
  for x0,x1,target in entradas:  # Entradas
    E = bias * wb + ((x0 * w0) + (x1 * w1))
    # Chave
    if (E > 0):
      saida = 1
    elif (E == 0):
      saida = 0
    elif (E < 0):
      saida = -1
    print(saida)
    if (saida == target):
      contador = contador + 1
  taxaacert = (contador / 4) * 100
  print("Taxa de acerto: ", taxaacert, "%")
  return 0


def TreinamentoAND(entradas):
  fim = 0
  j = 0
  i=0
  taxaaprend = 1
  w0 = 0
  w1 = 0
  w2 = 0
  wb = 0
  saida = 0
  E = 0
  bias = 0
  ##Área para colocar a combinação a ser treinada

  while (fim < 4):  # Ciclos
    fim = 0
    j = j + 1
    print("Ciclo: ", j)
    for x0,x1,target in entradas:  # Entradas
      print("Entrada ", i + 1)
      E = bias * wb + ((x0 * w0) + (x1 * w1))
      print("Target= ", target)
      # Chave
      if (E > 0):
        saida = 1
      elif (E == 0):
        saida = 0
      elif (E < 0):
        saida = -1
      print("Saida= ", saida)
      if (saida != target):
        print("Erro!")
        w0 = w0 + (taxaaprend * (target - saida)) * x0
        print("w0= ", w0)
        w1 = w1 + (taxaaprend * (target - saida)) * x1
        print("w1= ", w1)
        wb = wb + (taxaaprend * (target - saida)) * bias
        print("wb= ", wb)
        bias = bias + (taxaaprend * (target - saida))
        print("bias= ", bias, "\n")
      else:
        fim = fim + 1
        print("Acerto!\n")
      i=i+1
  TestesAND(w0, w1, w2, wb, bias,AND['entradaTestes'])


# Escreva o circuito lógico a ser testado
AND = {
    'entradaTreinamento': [
        [ -1, -1, -1],
        [ -1, 1, -1],
        [ 1, 1, 1],
        [1, -1, -1]
    ],
    'entradaTestes': [
        [ -1, 1, -1],
        [ -1, -1, -1],
        [ 1, -1, -1],
        [1, 1, 1]
    ]
}
TreinamentoAND(AND['entradaTreinamento'])