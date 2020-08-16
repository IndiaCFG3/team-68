# Writing to an excel 
# sheet using Python 
import xlwt 
from xlwt import Workbook 

# Workbook is created 
wb = Workbook() 

# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 

name = 'Manas'
email = 'saxenamanas0@gmail.com'

sheet1.write(0, 0, 'Name') 
sheet1.write(0,1,name)
sheet1.write(1, 0, 'Email') 
sheet1.write(1, 1, email)


wb.save('result.xls') 
