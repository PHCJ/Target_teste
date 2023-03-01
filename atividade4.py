# Valores de faturamento mensal por estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calculando o valor total mensal da distribuidora
total = sum(faturamento.values())

print(f"\nTotal Faturado: R${total:.2f}")

# Calculando e imprimindo o percentual de representação de cada estado
for estado, valor in faturamento.items():
    percentual = (valor / total) * 100
    print(f"{estado}: {percentual:.2f}%")
