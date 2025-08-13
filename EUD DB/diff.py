import csv

with open("armoha.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    data1 = list(reader)

with open("farty1billion_20221204162107.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    data2 = list(reader)

offset1 = [row[0] for row in data1]
offset2 = [row[0] for row in data2]

for offset in offset1:
    if offset not in offset2:
        print(f"Offset {offset} is not in farty1billion_20221204162107.csv")

for offset in offset2:
    if offset not in offset1:
        print(f"Offset {offset} is not in armoha.csv")
