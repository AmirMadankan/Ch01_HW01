import numpy as np
import matplotlib.pyplot as plt
from openpyxl import load_workbook, Workbook

ws = load_workbook("files/exp.xlsx")["Sheet1"]
max_row = ws.max_row

data = []
for i in range(1, max_row+1):
    data.append([ws[f"A{i}"].value, ws[f"B{i}"].value])

data = np.array(data)
x = data[:, 0]
y = data[:, 1]

dy = y[1:] - y[:-1]
dx = x[1:] - x[:-1]

yprime = y.copy()
yprime[1:] = dy/dx
yprime[0] = yprime[1]

