import numpy as np
import matplotlib.pyplot as plt
from openpyxl import load_workbook, Workbook

ws = load_workbook("files/exp.xlsx")["Sheet1"]
max_row = ws.max_row
