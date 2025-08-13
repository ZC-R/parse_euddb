import csv

with open("armoha.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    data1 = list(reader)

with open("farty1billion_20221204162107.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    data2 = list(reader)

offset1 = {row[0]: row for row in data1}
print(len(data1), len(offset1))
offset2 = {row[0]: row for row in data2}

for offset in offset1.keys():
    if offset not in offset2:
        print(f"Offset {offset} is not in farty1billion_20221204162107.csv")

for offset in offset2.keys():
    if offset not in offset1:
        print(f"Offset {offset} is not in armoha.csv")

for offset in offset2.keys():
    if offset in offset1:
        # name, size, length, description
        for x in range(3, 7):
            if offset1[offset][x - 1] != offset2[offset][x]:
                print(
                    f"Offset {offset} differs in column {x}: {offset1[offset][x - 1]} vs {offset2[offset][x]}"
                )


offsetS = offset1.keys() | offset2.keys()


with open("boratw.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    datas = list(reader)
offset3 = {row[-1]: row for row in datas}
for offset in offset3.keys():
    offset = offset[2:].zfill(8)
    if offset not in offsetS:
        print(f"Offset {offset} is only in boratw.csv")

with open("edac31433.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    datas = list(reader)
offset4 = {row[0]: row for row in datas}
for offset in offset4.keys():
    if offset not in offsetS:
        print(f"Offset {offset} is only in edac31433.csv")
