import xlrd
import re

rbook = xlrd.open_workbook('../shouyi.xls')
rbook.sheets()
rsheet = rbook.sheet_by_index(0)

print(rsheet)

colnames = rsheet.row_values(2)

fundCode = [i for i in colnames if i != '']

print(colnames)
print(fundCode)
#
# for row in rsheet.get_rows():
#     fundCode_column = row[1]
#     fundCode_value = fundCode_column.value
#
#     print(fundCode_value)