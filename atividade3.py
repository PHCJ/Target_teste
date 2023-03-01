import json

with open('dados.json', 'r') as file:
    dados = json.load(file)

# Encontra o valor máximo de faturamento
max_faturamento = min(dia['valor'] for dia in dados if dia['valor'] > 0)
for dia in dados:
    if dia['valor'] > 0 and dia['valor'] > max_faturamento:
        max_faturamento = dia['valor']

# Encontra o valor mínimo de faturamento
min_faturamento = max(dia['valor'] for dia in dados if dia['valor'] > 0)
for dia in dados:
    if dia['valor'] > 0 and dia['valor'] < min_faturamento:
        min_faturamento = dia['valor']

# Calcula a média de faturamento considerando apenas os dias com faturamento
dias_com_faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]
media_faturamento = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Conta o número de dias em que o valor de faturamento diário foi superior à média mensal
dias_acima_da_media = sum(1 for dia in dados if dia['valor'] > media_faturamento)

print("Valor máximo de faturamento:", max_faturamento)
print("Valor mínimo de faturamento:", min_faturamento)
print("Dias com faturamento acima da média:", dias_acima_da_media)