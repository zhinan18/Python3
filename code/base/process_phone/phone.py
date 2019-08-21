import openpyxl

phoneList = openpyxl.load_workbook("201908161.xlsx")
sheet = phoneList.worksheets[0]
i = 0
count = 0
dCount = 0
delList = list()
for cell in list(sheet.columns)[1]:
    i = i + 1
    phoneStr = str(cell.value).replace(" ", "")
    if len(phoneStr) != 11:
        count = count + 1
        phoneStr = phoneStr.strip(' ')
        if not phoneStr.__contains__("+86"):
            dCount = dCount + 1
            delList.append(i)
        else:
            if len(phoneStr) == 14:
                phoneStr = phoneStr[3:]
            elif len(phoneStr) == 15:
                phoneStr = phoneStr[4:]
            elif len(phoneStr) == 26:
                phoneStr = phoneStr[15:]
            print(phoneStr, "l:", str(len(phoneStr)))
            sheet.cell(i, 2, phoneStr)


print(count)
print(dCount)
print(delList)
file1 = open("delPhone1.txt", 'w')
file1.write(delList.__str__())
file1.close()

#phoneList.save("201908161.xlsx")



