import openpyxl 
wb = openpyxl.load_workbook('景区w.xlsx')
sheet = wb['景区天气']
lst=[]
for row in sheet.iter_rows():
    sub_lst=[]
    for cell in row:
        sub_lst.append(cell.value)
    lst.append(sub_lst)

for i in lst:
    print(i)