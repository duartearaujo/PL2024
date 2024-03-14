import sys
import re
import ply.lex as lex
import json
from decimal import Decimal


file = open('maquina.json', 'r')
data = json.load(file)
inventario = data['produtos']
moedas_maquina = data['moedas'][0]
produtos = {produto["id"]: produto for produto in inventario}

saldo = 0

tokens = (
    'LISTAR',
    'MOEDA',
    'SELECT',
    'ADICIONAR',
    'SAIR'
)

t_LISTAR = r'LISTAR'
t_MOEDA = r'MOEDA[ ]((1c|2c|5c|10c|20c|50c|1€|2€)[ ]?)+'
t_SELECT = r'SELECT[ ](\d+)'
t_ADICIONAR = r'ADICIONAR[ ](\d+)[ ](\d+)'
t_SAIR = r'SAIR'

t_ignore = ' \t\n'

def t_error(t):
    print(f'Caracter ilegal: {t.value[0]}')
    t.lexer.skip(1)

# Função para converter o valor das moedas para decimal
def handle_money(value):
    v = value
    if value[-1] == 'c':
        v = f"0.{value[:-1]}"
    elif value[-1] == '€':
        v = value[:-1]
    return Decimal(v)

# Função para atualizar o ficheiro json
def update_json():
    data['moedas'][0] = moedas_maquina
    for p in inventario:
        p['stock'] = produtos[p['id']]['stock']
    data['produtos'] = inventario
    file = open('maquina.json', 'w')
    json.dump(data, file, indent=4)
    file.close()

def handle_token(tok):
    global saldo

    # Print da tabela de produtos
    if tok.type == 'LISTAR':
        print('    ID     |        Produto        |    Stock    |    Preço   ')
        print('---------------------------------------------------------------')
        for id, produto in produtos.items():
            print(f"    {produto['id']: <5}  |       {produto['nome']: <10}      |    {produto['stock']: <5}    |    {produto['preco']: <5}")

    # Adicionar moedas à máquina
    elif tok.type == 'MOEDA':
        lmoedas = tok.value.split(' ')[1:]
        for moeda in lmoedas:
            saldo += handle_money(moeda)
            moedas_maquina[moeda] += 1
        print(f'SALDO {saldo}')

    # Comprar um produto
    elif tok.type == 'SELECT':
        id = int(tok.value.split(' ')[1])
        preco = handle_money(produtos[id]['preco'])
        r = saldo - preco
        if produtos[id]['stock'] == 0:
            print('Produto esgotado')
        elif r < 0:
            print('Saldo insuficiente')
        else:
            saldo = r
            produtos[id]['stock'] -= 1
            print(f'SALDO {saldo}')

    # Adicionar stock a um produto
    elif tok.type == 'ADICIONAR':
        id = int(tok.value.split(' ')[1])
        qtd = int(tok.value.split(' ')[2])
        produtos[id]['stock'] += qtd
        update_json()

    # Devolver o troco
    elif tok.type == 'SAIR':
        temp = saldo
        troco = []
        for moeda, qtd in moedas_maquina.items():
            m = handle_money(moeda)
            while (temp - m) >= 0 and qtd > 0:
                temp -= handle_money(moeda)
                qtd -= 1
                troco.append(moeda)
        if temp != 0:
            print('Não é possível devolver o troco na totalidade :(')
        for moeda in troco:
            moedas_maquina[moeda] -= 1
        saldo = 0
        update_json()
        print(f'TROCO {troco}')

lexer = lex.lex()
for line in sys.stdin:
    lexer.input(line)
    for tok in lexer:
        handle_token(tok)
    


