import os
import csv

bank_path = os.fspath("D:/Kunal/source/repo/learning/dsa/stw_assignment/bank_statement.csv")
# bank_data = os.read(bank_path, "r")

bank_amount = []
bank_date = []
with open(bank_path,newline= '') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[2] != "Amount": 
            bank_amount.append(row[2])
            bank_date.append(row[1])
            # print(row)

print(bank_amount)
print(bank_date)

software_path = os.fspath("D:/Kunal/source/repo/learning/dsa/stw_assignment/software_statement.csv")
# bank_data = os.read(bank_path, "r")

software_amount = []
software_date = []
with open(software_path, newline= '') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[2] != "Amount": 
            software_amount.append(row[2])
            software_date.append(row[1])
            # print(row)

print(software_amount)
print(software_date)

for i in bank_amount:
    for j in software_amount:
        if i == j:
            for i in bank_date:
                for j in software_date:
                    if i == j:
                        print("Match")
                        break
        break
            












# with open(bank_path, newline='') as f:
#     reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
#     for row in reader:
#         print(row)
