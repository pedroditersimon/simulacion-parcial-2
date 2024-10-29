"""
Erosión de Metas
Crea un programa que inicie con una meta de 50 y la reduzca en 5 unidades por iteración, deteniéndose al llegar o bajar de 10.
"""


def main():
  valor_actual = 50
  while valor_actual > 10:
    print(f"Valor actual {valor_actual}")
    valor_actual -= 5
  print(f"Valor final {valor_actual}")