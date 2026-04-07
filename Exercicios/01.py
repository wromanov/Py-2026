"""
Exercício 1 — Monitoramento de Ativos
A equipe de infraestrutura monitora 12 switches. Na última varredura, 9 estão online e 3 offline.
Crie um programa que calcule a disponibilidade da rede.
Fórmula (texto):
Ativos Online
Disponibilidade = -------------- x 100
Total de Ativos
"""

sw_ativos = 9
sw_indisponiveis = 3
total_ativos = sw_ativos + sw_indisponiveis
calc_disponibilidade = (sw_ativos / total_ativos) * 100
print(f"A disponibilidade dos ativos é {calc_disponibilidade}%")
