def TestesAND(w0, w1, wb, bias, entradas):
  sai=[]
  E = 0
  for x0,x1 in entradas:  # Entradas
    x0=int(x0)
    x1=int(x1)
    bias= int(bias)
    wb= int(wb)
    E = bias * wb + ((x0 * w0) + (x1 * w1))
    if (E > 0):
      saida = 1
    elif (E <= 0):
      saida = -1
    sai.append(saida)
  saida1=sai[0]
  saida2=sai[1]
  saida3=sai[2]
  saida4=sai[3]
  return saida1,saida2,saida3,saida4


def TreinamentoAND(entradas):
  fim = 0
  taxaaprend = 1
  w0 = 0
  w1 = 0
  wb = 0
  saida = 0
  E = 0
  bias = 0
  ##Área para colocar a combinação a ser treinada

  while (fim < 4):  # Ciclos
    fim = 0
    for x0,x1,target in entradas:  # Entradas
      x0=int(x0)
      x1=int(x1)
      target=int(target)
      E = bias * wb + ((x0 * w0) + (x1 * w1))
      # Chave
      if (E > 0):
        saida = 1
      elif (E <= 0):
        saida = -1
      if (saida != target):
        w0 = w0 + (taxaaprend * (target - saida)) * x0
        w1 = w1 + (taxaaprend * (target - saida)) * x1
        wb = wb + (taxaaprend * (target - saida)) * bias
        bias = bias + (taxaaprend * (target - saida))
      else:
        fim = fim + 1
  return w0,w1,wb,bias

