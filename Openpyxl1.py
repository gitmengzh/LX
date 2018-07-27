#coding:utf-8


from openpyxl import workbook
from openpyxl import load_workbook
from openpyxl.writer.excel import ExcelWriter

wb = load_workbook(filename = r'C:\Users\meng4\Desktop\test\test.xlsx')
ws = wb.get_sheet_by_name("Sheet1")
for i in range(1,35):
    ls = []
    for row_num in xrange (1,40):
       c1 = int(ws.cell (row = row_num, column = 1).value)
       c2 = ws.cell (row = row_num, column = 2).value
       '''total = int (c1) + int (c2)
       ws.cell (row = i, column = 4 ).value = total'''

wb.save(filename = dest_filename)

