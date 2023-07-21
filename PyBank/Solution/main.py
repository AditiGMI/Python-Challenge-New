#import csv & os
import os
import csv

#open csv file
budget_csv = os.path.join("..", "Resources", "budget_data.csv")

#defining variable for results

Months = []
Total_months = 0
Total_profit_loss = 0
Current_month_profit_loss = 0
Previous_month_profit_loss = 0
Profit_loss_changes = []
Profit_loss_change = 0
Average_change = 0
Greatest_increase_in_Profits = []
Greatest_decrease_in_Profits = []

#reading the first line of the csv file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
   
#counting the total number of months 
        Total_months += 1

#Total profit loss calculation   
        Current_month_profit_loss = int(row[1]) 
        Total_profit_loss += Current_month_profit_loss
        if (Total_months == 1):
             Previous_month_profit_loss = Current_month_profit_loss
             continue

        else: 
             Profit_loss_change = Current_month_profit_loss - Previous_month_profit_loss
             Months.append(row[0])
             Profit_loss_changes.append(Profit_loss_change)
             Previous_month_profit_loss = Current_month_profit_loss 

#Total & average profit & loss calculation       
Total_profit_loss = sum(Profit_loss_changes)
Average_change = Total_profit_loss / Total_months                          

#Greatest increase & decrease calculation
Greatest_increase_in_Profits = max(Profit_loss_changes)
Greatest_decrease_in_Profits = min(Profit_loss_changes)  

#printing the results
print("Financial Analysis")
print("-------------------------")
print(f"Total months: {Total_months}")
print(f"Total amount: {Total_profit_loss}")
print(f"Average Change: {Average_change}")
print(f"Greatest increase: {Greatest_increase_in_Profits}")
print(f"Greatest Decrease: {Greatest_decrease_in_Profits}")

# open the output file, then write 
f = open("output.txt", "w")
f.write("Financial Analysis")
f.write("-------------------------")
f.write(f"Total months: {Total_months}")
f.write(f"Total amount: {Total_profit_loss}")
f.write(f"Average Change: {Average_change}")
f.write(f"Greatest increase: {Greatest_increase_in_Profits}")
f.write(f"Greatest Decrease: {Greatest_decrease_in_Profits}")
  
