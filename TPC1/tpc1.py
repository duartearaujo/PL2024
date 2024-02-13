file = "emd.csv"

with open(file, "r") as f:
    lines = f.readlines()

    data = []

    for line in lines[1:]:
        data.append(line.strip().split(","))

aptos = 0
modalidades = []
escalao1 = []
escalao2 = []
escalao3 = []

for elem in data:
    if (elem[12] == "true"):
        aptos += 1
    if elem[8] not in modalidades:
        modalidades.append(elem[8])
    
    idade = int(elem[5])
    if 30 <= idade <= 34:
        escalao1.append(elem[0])
    elif 35 <= idade <= 39:
        escalao2.append(elem[0])
    elif 40 <= idade <= 44:
        escalao3.append(elem[0])

modalidades.sort()
percentagem = aptos * 100 / len(data)
print(f"Percentagem de atletas aptos: {percentagem}\n")
print(f"Percentagem de atletas inaptos: {100 - percentagem}\n")
print(f"Modalidades: {modalidades}\n")
print(f"Atletas escalão 1: {escalao1}\n")
print(f"Atletas escalão 2: {escalao2}\n")
print(f"Atletas escalão 3: {escalao3}\n")
