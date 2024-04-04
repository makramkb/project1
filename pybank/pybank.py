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
monthly_change = []
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
        monthly_change_value = float(pl_data[j-1])-float(pl_data[j])
        monthly_change.append(monthly_change_value)
    inc_date = date_data[monthly_change.index(max(monthly_change))]
    dec_date = date_data[monthly_change.index(min(monthly_change))]
    print(f'greatest inc in value is {max(monthly_change)} that happened on {inc_date}')
    print(f'the least increase in values is {min(monthly_change)} that happened on {dec_date}')

analysis_path = os.path.join('..','pybank','The_analysis.txt')
with open(analysis_path,'w') as analysis_txt:
    analysis_txt.write(f'This is the findings of the pybank data file :\n')
    analysis_txt.write('\n')
    analysis_txt.write(f'The total number of month in this data is {total}\n')
    analysis_txt.write('\n')
    analysis_txt.write(f'The profit/Loss for the entire peiod is : {profit_loss}$\n')
    analysis_txt.write('\n')
    analysis_txt.write(f'The avg p/l for the total period is : {avg_pl}$\n')
    analysis_txt.write('\n')
    analysis_txt.write(f'The greatest increase happened in {inc_date} with an amount of {max(monthly_change)}$\n')
    analysis_txt.write('\n')
    analysis_txt.write(f'Finaly the greatest decrease happened in {dec_date} with an amount of {min(monthly_change)}$')
   
    
  

