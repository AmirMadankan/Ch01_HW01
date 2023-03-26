import numpy as np
import matplotlib.pyplot as plt
from openpyxl import load_workbook, Workbook

ws = load_workbook("files/x2.xlsx")["Sheet1"]
max_row = ws.max_row

data = []
for i in range(1, max_row+1):
    data.append([ws[f"A{i}"].value, ws[f"B{i}"].value])

data = np.array(data)
x = data[:, 0]
y = data[:, 1]

dy = y[1:] - y[:-1]
dx = x[1:] - x[:-1]

ddy = dy[1:] - dy[:-1]
ddx = dx[1:] - dx[:-1]

yprime = y.copy()
yprime[1:] = dy/dx
yprime[0] = yprime[1]

ydoubleprime = yprime.copy()
ydoubleprime[2:] = ddy/ddx
# ydoubleprime[0] = ydoubleprime[1]

# wb_save = Workbook()
# ws_save = wb_save.active
# wb_save2 = Workbook()
# wb_save2 = wb_save2.active

# i = 0
# for x_i in x:
#     ws_save[f"A{i+1}"] = x_i
#     ws_save[f"B{i+1}"] = yprime[i]
#     wb_save2[f"A{i+1}"] = x_i
#     wb_save2[f"B{i+1}"] = ydoubleprime[i]
#     i += 1

# wb_save.save("files/dexp.xlsx")
# wb_save2.save("files/ddexp.xlsx")

# plt.plot(x, y, label="exp(x)")
# plt.plot(x, yprime, label="dexp(x)")
# plt.plot(x, ydoubleprime, label="ddexp(x)")
# plt.legend()
# plt.title("exp(x) & dexp(x) & ddexp(x)")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()