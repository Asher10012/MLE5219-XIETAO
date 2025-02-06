import weather
import openpyxl
html=weather.get_html()
lst=weather.parse_html(html)
wb=openpyxl.Workbook()
sheet=wb.create_sheet('景区天气')
for i in lst:
    sheet.append(i)

wb.save('景区w.xlsx')