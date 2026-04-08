"""
Exercício 18 — Aprovação escolar
Calcule a média de 7.5, 6.0 e 8.0 e informe aprovação.
"""

nota1 = 7.5
nota2 = 6.0
nota3 = 8.0

media = (nota1 + nota2 + nota3) / 3

if media >= 5:
    print(f"Media {media:.2f} | Status: Aprovado")
else:
    print(f"Media {media:.2f} | Status: Reprovado")

