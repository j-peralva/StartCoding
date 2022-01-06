"""
:author 'Jefferson Peralva Machiqueira':
Link para o vídeo: https://youtu.be/Z7Jo4Ft2HeA
A solução apresentada atende aos requisitos da disciplina Fundamentos de Programação? Sim
"""

from math import pi


distancia_km = int(input("Entre com a distância em quilômetros: "))
diameter_cm = int(input("Entre com o diâmetro em centímetros: "))
diameter_km = diameter_cm * 10**-5
comprimento = round(pi, 3) * diameter_km
numero_voltas = distancia_km / comprimento
m, n = tuple(map(float, f"{numero_voltas:e}".split("e")))
if m >= 3.16:
    n += 1
print(f"Distância percorrida: {distancia_km} km")
print(f"Diâmetro da roda: {diameter_cm} cm")
print(f"Ordem de grandeza da quantidade de voltas efetuadas: 10 elevado a {int(n)}")
