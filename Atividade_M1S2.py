# Caixa do bar do Sr. João

# Demonstrar o total em R$ que o caixa possui em moedas.
# float

total_5_centavos = 35 * 0.05
total_10_centavos = 50 * 0.1
total_25_centavos = 30 * 0.25
total_50_centavos = 15 * 0.5
total_1real = 19 * 1

total_caixa = float(
    total_5_centavos + total_10_centavos + total_25_centavos + total_50_centavos + total_1real
)

print(f'{total_caixa:.2f}')