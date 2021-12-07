# import json
# import pandas as pd
#
# df = pd.read_excel('Arhamatadararu.xlsx', skiprows=6)
#
# result = df.to_json(orient="records")
# data = json.loads(result)
# print(data)
import pandas as pd
from openpyxl import load_workbook
import json
import pandas as pd

df = pd.read_excel('SHAREE LIST.xlsx', sheet_name="Sheet2", skiprows=1)

result = df.to_json(orient="records")
data = json.loads(result)
# print(data[0]['sr'])
nt = load_workbook('Arhamatadararu.xlsx')

name = "Sheet1"
sheet = nt[name]
print(len(data))
for i in range(913):
    b = f"B{7+i}"
    c = f"C{7+i}"
    d = f"D{7+i}"
    e = f"E{7+i}"
    f = f"F{7+i}"
    h = f"H{7+i}"
    k = f"I{7+i}"
    sheet[b] = f"{str(data[i]['n1']).strip()} {str(data[i]['n2']).strip()} {str(data[i]['n3']).strip()}"
    sheet[c] = str(data[i]['n4']).split(' ')[0]
    sheet[d] = data[i]['n5']
    sheet[e] = i+1
    sheet[f] = data[i]['n7']
    sheet[h] = data[i]['n8']
    sheet[k] = data[i]['n6']

nt.save("new1.xlsx")
nt.close()