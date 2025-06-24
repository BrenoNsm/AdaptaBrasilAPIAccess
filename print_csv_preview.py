import csv
import argparse

parser = argparse.ArgumentParser(description='Mostra as primeiras linhas do CSV gerado pelo AdaptaBrasilAPIAccess.')
parser.add_argument('arquivo', help='Arquivo CSV a ser exibido')
parser.add_argument('-n', '--num-linhas', type=int, default=5, help='Número de linhas a serem exibidas')

args = parser.parse_args()

with open(args.arquivo, encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter='|')
    for i, row in enumerate(reader, start=1):
        print(f'Linha {i}:')
        for campo, valor in row.items():
            print(f'  {campo}: {valor}')
        print()
        if i >= args.num_linhas:
            break
