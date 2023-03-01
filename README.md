# Repositório Teste Target

Este repositório contém soluções para exercícios propostos. As soluções são implementadas em Python e estão divididas em vários arquivos.

## Tecnologias

Python 3.9.13

## Como executar

Para executar o programa, basta rodar o comando `python app.py` no terminal. Em seguida, escolha uma das opções do menu e siga as instruções apresentadas.

## Módulos

### app.py

O arquivo app.py é um programa que apresenta um menu com opções de exercícios a serem executados. As opções do menu são:

- Pergunta 2 (atividade2.py)
- Pergunta 3 (atividade3.py)
- Pergunta 4 (atividade4.py)
- Pergunta 5 (atividade5.py)
- Sair

### atividade2.py

Este módulo contém uma função `fibonacci(n)` que verifica se um determinado número pertence à sequência de Fibonacci.

### atividade3.py

Este módulo lê dados de um arquivo JSON e calcula o valor máximo, mínimo e médio de faturamento, bem como o número de dias em que o valor de faturamento foi superior à média mensal.

### atividade4.py

Este módulo calcula o faturamento mensal de uma distribuidora de energia elétrica por estado e exibe o total faturado, bem como o percentual de representação de cada estado.

### atividade5.py

Este módulo recebe um texto e o inverte.

### Arquivo dados.json

O arquivo dados.json contém informações sobre o faturamento de uma empresa por dia. Cada entrada do arquivo representa um dia e contém as seguintes informações:

- data: data no formato dd/mm/yyyy
- valor: valor do faturamento no dia

O arquivo é lido pelo código contido no arquivo atividade3.py.

