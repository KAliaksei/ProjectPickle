import pandas as pd
import xlrd

# The webpage URL whose table we want to extract 
url = "https://finance.yahoo.com/quote/AAPL/history/"
  
# Assign the table data to a Pandas dataframe 
table = pd.read_html(url)[0] 
table.to_excel("data1.xlsx")

loc = ('data1.xlsx')
loc1 = ('companylist.csv.xlsx')
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet1 = wb.sheet_by_index(0)
wb1 = xlrd.open_workbook(loc1)
dataset = []
length = 1
while length != 31:
    if "Dividend" in sheet.cell_value(length,5):
       break
    else:        
        dataset.append(float(sheet.cell_value(length,5)))
        length+=1

print(dataset)
