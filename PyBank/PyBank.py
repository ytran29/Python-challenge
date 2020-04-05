
import os
import csv
filepath = os.path.join ("..", "Resources", "budget_data.csv")
with open (filepath) as csvfile:
    PyBank_data = csv.reader(csvfile, delimiter=',')
    csv_header = next (PyBank_data)
    csv_firstrow = next (PyBank_data)
    Pre_amount = int(csv_firstrow[1])
    count = 1
    total_amount = Pre_amount
    change_amounts =[]
    date_values = []
    for row in PyBank_data:
        count = count +1
        date_values.append(row[0])
        total_amount = (total_amount + int(row[1]))
        change_amounts.append(int(row[1])-Pre_amount)
        Pre_amount = int(row[1])
    Average_change = round (sum(change_amounts)/len(change_amounts),2)
    Greatest_Increase = max(change_amounts)
    Greatest_Increase_day = date_values[change_amounts.index (Greatest_Increase)]
    Greatest_Decrease = min(change_amounts)
    Greatest_Decrease_day = date_values[change_amounts.index (Greatest_Decrease)]

#for row in change_amounts
    Result = ""
    print(f'Total Months: {count}')
    Result += f'Total Months: {count}\n'
    print(f'Total: $ {total_amount}')
    Result += f'Total: $ {total_amount}\n'
    print(f'Average Change: $ {Average_change}')
    Result += f'Average Change: $ {Average_change}\n'
    print(f'Greatest Increase in Profit: {Greatest_Increase_day} (${Greatest_Increase})')
    Result += f'Greatest Increase in Profit: {Greatest_Increase_day} (${Greatest_Increase}\n'
    print(f'Greatest Decrease in Profit: {Greatest_Decrease_day} (${Greatest_Decrease})')
    Result += f'Greatest Decrease in Profit: {Greatest_Decrease_day} (${Greatest_Decrease})'

with open("PyBank_Report.txt","w") as report:
    report.write (Result)
    
        
    
    


      
    
        
        
        
       
     
     
       