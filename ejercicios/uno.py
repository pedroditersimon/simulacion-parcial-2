"""
Programa de Decremento con Conteo de Iteraciones:
Crea un programa en Python que inicie con un valor inicial de 50. El programa debe reducir este valor en 10 unidades por iteración y mostrar el valor restante después de cada decremento. El proceso continuará hasta que el valor llegue a 0. Al finalizar, el programa debe indicar cuántas iteraciones fueron necesarias para alcanzar el 0.
"""


def main():
  valor_inicial = 50

  decremento = 10
  valor_actual = valor_inicial
  iteraciones = 0

  while valor_actual > 0:
    valor_actual -= decremento
    iteraciones += 1
    print(f"Valor restante {valor_actual}")

  print(f"Iteraciones {iteraciones}")
