def TestesAND(w0, w1, w2, wb, bias):
  print("Pesos aprendidos: ({}, {}, {})".format(w0, w1, w2))
  contador = 0
  saida = 0
  E = 0
  ##Área para colocar as combinações a serem testadas
  target = [-1, -1, -1, 1]
  x0 = [-1, -1, 1, 1]
  x1 = [1, -1, -1, 1]
  for i in range(0, 4):  # Entradas
    E = bias * wb + ((x0[i] * w0) + (x1[i] * w1))
    # Chave
    if (E > 0):
      saida = 1
    elif (E == 0):
      saida = 0
    elif (E < 0):
      saida = -1

    if (saida == target[i]):
      contador = contador + 1
  taxaacert = (contador / 4) * 100
  print("Taxa de acerto: ", taxaacert, "%")
  return 0


def TreinamentoAND():
  fim = 0
  j = 0
  taxaaprend = 1
  w0 = 0
  w1 = 0
  w2 = 0
  wb = 0
  saida = 0
  E = 0
  bias = 0
  ##Área para colocar a combinação a ser treinada
  target = [-1, -1, 1, -1]
  x0 = [-1, -1, 1, 1]
  x1 = [-1, 1, 1, -1]

  while (fim < 4):  # Ciclos
    fim = 0
    j = j + 1
    print("Ciclo: ", j)
    for i in range(0, 4):  # Entradas
      print("Entrada ", i + 1)
      E = bias * wb + ((x0[i] * w0) + (x1[i] * w1))
      print("Target= ", target[i])
      # Chave
      if (E > 0):
        saida = 1
      elif (E == 0):
        saida = 0
      elif (E < 0):
        saida = -1
      print("Saida= ", saida)
      if (saida != target[i]):
        print("Erro!")
        w0 = w0 + (taxaaprend * (target[i] - saida)) * x0[i]
        print("w0= ", w0)
        w1 = w1 + (taxaaprend * (target[i] - saida)) * x1[i]
        print("w1= ", w1)
        wb = wb + (taxaaprend * (target[i] - saida)) * bias
        print("wb= ", wb)
        bias = bias + (taxaaprend * (target[i] - saida))
        print("bias= ", bias, "\n")
      else:
        fim = fim + 1
        print("Acerto!\n")
  TestesAND(w0, w1, w2, wb, bias)


#Escreva o circuito lógico a ser testado
TreinamentoAND()
