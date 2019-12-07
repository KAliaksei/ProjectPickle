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

        else:
            counter += 1
        if counter == 3312:
            print("Company not found")
            break
    return url

usersearchcheck(entry)
#usersearch = input("What company do you want to analyze?")
# Assign the table data to a Pandas dataframe
table = pd.read_html(usersearchcheck(entry))[0]
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


def insert(root, Node):
    if root is None:
        root = Node
    else:
        if root.value < Node.value:
            if root.right is None:
                root.right = Node
            else:
                insert(root.right, Node)
        else:
            if root.left is None:
                root.left = Node
            else:
                insert(root.left, Node)

def build_tree(list):
    r = Node(list[0])
    for numbers in list[1:]:
        insert(r,Node(numbers))
    return r

print(build_tree(dataset))
