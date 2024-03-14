# TPC4

## Analisador Léxico

**Nome:** Duarte Araújo
**Número:** A100750

## Explicação

O trabalho consiste na elaboração de um analisador léxico que consiga distinguir diferentes tokens de uma query. Neste caso, deverá reconhecer instruções SQL, como é o caso do `SELECT..FROM..WHERE`, atributos de entidades, operadores lógicos, números e vírgulas.

Foi utilizada a biblioteca `ply` na resolução deste trabalho, de modo a facilitar o reconhecimento dos tokens no texto recebido pelo stdin.

## Comando a executar

**cat [nome do ficheiro].txt | python3 tpc4.py**
