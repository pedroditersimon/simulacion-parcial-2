"""
Retroalimentación Positiva
Escribe un programa que inicie con un valor de 1 y lo duplique continuamente hasta que supere el valor de 100. Al superar 100, el programa debe reducir el valor en 3 unidades antes de detenerse.
"""


def main():
  valor = 1

  while True:
    if valor * 2 < 100:
      valor *= 2
    else:
      valor -= 3
      break

    print(f"Valor actual {valor}")

  print(f"Valor final {valor}")
