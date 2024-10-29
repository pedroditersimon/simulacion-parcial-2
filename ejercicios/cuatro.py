"""
Simulación de Adicciones
Crea un programa que simule el crecimiento de un hábito a lo largo de 5 días. En cada día, el hábito se refuerza en 1 unidad. Sin embargo, si el número del día es múltiplo de 3 (por ejemplo, el día 0 o el día 3), ocurre una recaída, y el hábito se reduce en 1 unidad.

El programa debe calcular el nivel final del hábito al terminar los 5 días e imprimirlo en pantalla.
"""

def main():
  habito = 0
  dia = 0
  for dia in range(5):
    es_multiplo = dia % 3 == 0
       
    if es_multiplo:
      habito -= 1
    else:
      habito += 1
    print(f"Dia {dia}, Habito {habito}")
    
  print(f"Nivel final {habito}")