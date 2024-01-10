# Quanto cobrar por 80 horas trabalhadas?

# Fórmula: valor inicial + quantidade de horas estimadas * valor da hora + 15% do valor calculado.

valor_inicial = 1000
valor_hora = 20.45
horas_estimadas = 80
taxa = 0.15

valor_calculado1 = valor_inicial + (horas_estimadas * valor_hora)
valor_calculado2 = valor_calculado1 * taxa
valor_total = valor_calculado1 + valor_calculado2

print(f'\n{valor_total:.2f}\n')
