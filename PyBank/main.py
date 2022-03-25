 
import os
import csv


csvpath = os.path.join("Resources","budget_data.csv")

data = []
total_net_profit = 0
total_months = 0
months_list = []
profit_change_list = []
greatest_increase = 0
greatest_decrease = 0

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    for row in csvreader:
        data.append(row)

# title of table and total months
for r in data:
    months_list.append(r[0])
total_months = len(months_list)
print("Financial Analysis")
print("---------------------------")
print("Total Months:", total_months)

# total net profit
for s in data:
    profit_change_list.append(r[0])
total_net_profit = total_net_profit + int(row[1])
print("Total:", total_net_profit)

# average change
average_change = total_net_profit/total_months
print("Average Change:", average_change)

# greatest increase and decrease
greatest_increase = max(profit_change_list)
greatest_decrease = min(profit_change_list)
print("Greatest Increase in Profits:", greatest_increase)
print("Greatest Decrease in Profits:", greatest_decrease)


# set variable for output file
output_file = os.path.join("budget_data.txt")

# open output text file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

# write header row
    writer.writerow(["Date", "Profit/Losses"])

# write in zipped rows
    writer.writerows(data)   