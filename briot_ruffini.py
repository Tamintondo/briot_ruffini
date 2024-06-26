# -*- coding: utf-8 -*-
"""Briot - ruffini.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BX9blUe0cWLfvtgJSiyj2lQE3zm3iC_S
"""

def briot_ruffini(polinomio, raiz):
  """
 Algoritmo de Briot-Ruffini para encontrar o resto da divisão de um polinômio de grau n por (x - raiz).

 Argumentos:
 polinômio: Uma lista de coeficientes do polinômio, ordenados do maior para o menor grau.
 raiz: O valor da raiz.

 Retorna:
 O resto da divisão do polinômio por (x - raiz).
 o polinômio restante da divisão de grau n-1
  """
  # Verificar se a raiz é válida.
  n = len(polinomio) -1
  soma = 0
  for i in range (0,n+1):
    soma = soma + polinomio[i]*(raiz**(n-i))

  # Limitar resultado apenas ao módulo.
  soma = abs(soma)

  # Caso o módulo soma seja maior que zero não é uma raiz.
  if soma > 0:
    raise ValueError("A raiz não é válida.")

  # Apenas raízes não nulas serão consideradas.
  if raiz == 0:
    raise ValueError("A raiz não pode ser zero.")

  # Verificar que o polinomio tenha ao menos um coeficiente.
  if len(polinomio) == 0:
    raise ValueError("O polinomio não pode estar vazio.")

  # Criar o restante da expressão
  novo_polinomio = []

  # Inicializar o resto com o coeficiente de maior grau.
  resto = polinomio[0]

  # Inicializar o novo polinomio de grau n-1
  novo_polinomio.append(resto)

  # Iterar sobre o restante do polinomio.
  for i in range(1, len(polinomio)):

    # Multiplicar o resto pela raiz.
    resto = resto * raiz

    # Somar o coeficiente atual ao resto.
    resto = resto + polinomio[i]

    if i < len(polinomio)-1:
      novo_polinomio.append(resto)

  # retorna o resto.
  return resto, novo_polinomio
