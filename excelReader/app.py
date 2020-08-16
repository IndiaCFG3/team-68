import xlrd
loc = ("./sheet.xlsx") 
  
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
# For row 0 and column 0 
typeOfData = sheet.cell_value(0, 1)
name = sheet.cell_value(1,1)
email = sheet.cell_value(2,1)

print(typeOfData + ' '+ name + ' '+email)


# EXCEL FILE - 
#      0        1
# 0   type    Student
# 1   name    Manas
# 2   email   saxenamanas0@gmail.com