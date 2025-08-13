import csv
import requests
from bs4 import BeautifulSoup

url = "https://armoha.github.io/eud-book/offset_table.html"
response = requests.get(url)

if response.status_code != 200:
    print(f"요청 실패: {response.status_code}")
    exit(1)

soup = BeautifulSoup(response.text, "html.parser")
table = soup.find("table")
if table is None:
    print("표를 찾을 수 없습니다.")
    exit(1)
rst = str(table)

rows = []
for tr in table.find_all("tr"):
    cells = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]
    if cells:
        rows.append(cells)
with open("armoha.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
print("CSV 파일로 저장되었습니다: armoha.csv")
