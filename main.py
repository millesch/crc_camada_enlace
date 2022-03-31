#Variaveis do cálculo
polinomio = '1001' #Polinomio em binário
chave = "101110000" #Chave
grau = 3 #Grau do polinomio

#Função que realiza o cálculo do polinomio
def crc(polinomio, grau, chave):
  
  #Auxiliares do cálculo do polinomio
  pos = len(polinomio) #Tamanho do polinomio
  temp = chave[0:pos] #Temporário, para auxílio na divisão
  loop = True #Enquanto loop verdadeiro
  aux = grau #Auxiliar com o valor de grau

  print("\nRestos da divisão: \n")
  
  while loop:

    #Auxiliar para o cálculo principal, ele irá verificar se não há mais posições ou bits para o cálculo
    if(aux <= 0):
      loop = False
    
    result = ''
    
    #Looping para XOR
    for x in range(grau+1):
      if ((polinomio[x] == '0' and temp[x] != '0') or (polinomio[x] == '1' and temp[x] != '1')):
        result += '1'
      else:
        result += '0'
        
    temp = result
    
    #Enquanto a primeira posição for zero, é retirado e adicionado mais uma posição da chave para realizar a divisão - Auxílio no resto da divisão
    while temp[0] == '0':
      temp = list(temp)
      for x in range(grau-1):
        temp[x] = temp[x + 1]
      if(len(chave) - pos > 0):
        temp[grau] = chave[pos]
      else:
        temp[grau] = '0'
        aux = aux - 1 #Diminui o aux conforme for adicionando zeros (caso não há mais bits na chave)
      temp = "".join(temp)
      pos += 1
    print(result)
    
  chave_nova = chave[:-grau] + result[1:] #A nova chave é o valor da chave com o seu final substituído pelo CRC

  return chave_nova #Retorno da chave para o destinatário


chave_modificada = crc(polinomio, grau, chave)
print("\nChave passada para o destinatário pós CRC: " + chave_modificada + "\n")

chave_retorno = crc(polinomio, grau, chave_modificada)
print("\nChave calculada pelo destinatário: " + chave_retorno + "\n")

if(chave_modificada == chave_retorno):
  print("Dados não modificados")
else:
  print("Os dados sofreram perdas")
  
