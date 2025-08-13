import csv
import json
import requests

url = "https://raw.githubusercontent.com/boratw/eudlist/refs/heads/main/data/Offset_Global.json"
response = requests.get(url)

if response.status_code != 200:
    print(f"요청 실패: {response.status_code}")
    exit(1)


data = json.loads(response.content.decode("utf-8-sig"))
keys = data["data"][0].keys()

with open("boratw.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(keys)  # header

    for row in data["data"]:
        # if row.keys() != keys:
        #     print("키가 일치하지 않습니다.")
        writer.writerow([row[key] for key in keys])
