"""
:author 'Jefferson Peralva Machiqueira':
Link para o vídeo: https://youtu.be/GgZw7qC2FaI
A solução apresentada atende aos requisitos da disciplina Fundamentos de Programação? Sim
"""

from math import pi
from typing import Union


def truncate(num: Union[int, float], n_digits: Union[int, None] = None) -> float:
    """
    Função para truncar um número
    :param num: Número a ser truncado
    :param n_digits: Número de casas decimais desejadas
    :return: retorna o valor truncado
    """
    if n_digits is None:
        n_digits = 0
    return float(f"{int(num * 10 ** n_digits) * 10 ** -n_digits:.{n_digits}f}")


distancia_km = int(input("Entre com a distância em quilômetros: "))
diameter_cm = int(input("Entre com o diâmetro em centímetros: "))
diameter_km = diameter_cm * 10**-5
perimeter = truncate(pi, 3) * diameter_km
numero_voltas = distancia_km / perimeter
m, n = (float(val) for val in f"{numero_voltas:e}".split("e"))
if m >= 3.16:
    n += 1
print(f"Distância percorrida: {distancia_km} km")
print(f"Diâmetro da roda: {diameter_cm} cm")
print(f"Ordem de grandeza da quantidade de voltas efetuadas: 10 elevado a {int(n)}")
