import openpyxl

workbook = openpyxl.load_workbook('ITEC_Courses.xlsx')

sheet_names = workbook.sheetnames
print(sheet_names)

codes_sheet = workbook.active

b2_data = codes_sheet['B2'].value

print(b2_data)

c5_data = codes_sheet['C5'].value

print(c5_data)

for row in codes_sheet.rows:
    for cell in row:
        print(cell.value)

print()

for col in codes_sheet.columns:
    for cell in col:
        print(cell.value)

# get all data from one colum

class_names_column = codes_sheet['C']

for cell in class_names_column:
    print(cell.value)
# get another sheet, by name
rooms_sheet = workbook['rooms']
room_column = rooms_sheet['B']
for cell in room_column:
    print(cell.value)

