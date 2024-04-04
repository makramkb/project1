#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period
import os
file = os.path.join("..","pybank","Resources","budget_data.csv")
import csv
date_data = []
pl_data = []
greatest_inc = []
with open(file,'r') as budget:
    csv_reader = csv.reader(budget,delimiter=',')
    header = next(budget)
    total=0
    profit_loss = 0
    for row in csv_reader:
        date_data.append(row[0])
        pl_data.append(float(row[1]))
        total = total + row.count(row[0])
        profit_loss = profit_loss + float(row[1])
    avg_pl = round(profit_loss/total,2)
    print(f'the total number of month in this data is {total}')
    print(f'the p/l for this period is : {profit_loss}')
    print(f'the avg is {avg_pl}')
    for j in range(len(pl_data)):
        greatest_inc_value = float(pl_data[j-1])-float(pl_data[j])
        greatest_inc.append(greatest_inc_value)
    inc_date = date_data[greatest_inc.index(max(greatest_inc))]
    dec_date = date_data[greatest_inc.index(min(greatest_inc))]
    print(f'greatest inc in value is {max(greatest_inc)} that happened on {inc_date}')
    print(f'the least increase in values is {min(greatest_inc)} that happened on {dec_date}')
   
    
  

