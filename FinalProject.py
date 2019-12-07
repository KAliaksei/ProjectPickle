import pandas as pd
import xlrd
from binarytree import Node
import math
# The webpage URL whose table we want to extract
entry = input("Enter company name to analyze")
def usersearchcheck(entry):
    entry= entry.title().capitalize()
    loc1 = ('companylist.csv.xlsx')
    wb1 = xlrd.open_workbook(loc1)
    sheet1 = wb1.sheet_by_index(0)
    i = 0
    g = 0
    counter = 0
    for i in range(sheet1.nrows):
        if entry in sheet1.cell_value(i,1):
            ticker = sheet1.cell_value(i, 0)
            url = ("https://finance.yahoo.com/quote/%s/history/" %ticker)
            print(url)
            return url
        else:
            counter += 1
        if counter == 3312:
            print("Company not found")
            break
    return url

def build_bst(list):
    if not list:
        return None

    # find middle
    mid = math.floor(int(len(list)) / 2)

    # make the middle element the root
    root = (Node(list[mid]))
    root.left = (build_bst(list[:mid]))
    root.right = (build_bst(list[mid + 1:]))
    return root
usersearchcheck(entry)
#usersearch = input("What company do you want to analyze?")
url = ("https://finance.yahoo.com/quote/AAPL/history/")
# Assign the table data to a Pandas dataframe 
table = pd.read_html(url)[0] 
table.to_excel("data1.xlsx")

loc = ('data1.xlsx')
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet1 = wb.sheet_by_index(0)
dataset = []
length = 1
while length != 31:
    if "Dividend" in sheet.cell_value(length,5):
       break
    else:        
        dataset.insert(0,float(sheet.cell_value(length,5)))
        length+=1

testlist = dataset


print(dataset)
#print(build_bst(testlist))
print(build_bst(testlist).pprint(index=True))

