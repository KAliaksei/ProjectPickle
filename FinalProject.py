import pandas as pd
import xlrd
from binarytree import Node
import math

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
def timeframe():
    stime = str(input("Enter W, M, or Q for weekly, monthly, or quartrly data analysis"))
    print(stime == "M")
    if (stime == "M"):
        stime = 30
        print(stime)
        return stime
    elif (stime =="W"):
        stime = 7
        print(stime)
        return stime
    elif (stime == "Q"):
        stime = 90
        print(stime)
        return stime
    else:
        print("Invalid value")
        timeframe()
    return stime
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
            runtime()
    return url
def runtime():
    while(True):
        entry = input("Enter company name to analyze")
        usersearchcheck(entry)
        table = pd.read_html(usersearchcheck(entry))[0]
        table.to_excel("data1.xlsx")

        loc = ('data1.xlsx')
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        sheet1 = wb.sheet_by_index(0)
        dataset = []
        length = 1
        length1 = timeframe()
        print(length1)
        while length != length1:
            if "Dividend" in sheet.cell_value(length,5):
                length+=1
                continue
            else:
                dataset.insert(0,float(sheet.cell_value(length,5)))
                length+=1

        testlist = dataset

        print(build_tree(dataset))
runtime()
