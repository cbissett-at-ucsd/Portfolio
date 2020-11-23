import filecmp
import openpyxl
wb= openpyxl.load_workbook("PDFcmp.xlsm")
ws=wb.active
print(ws['A1'])
