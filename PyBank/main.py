import os

import csv

csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
#print(csvreader)'
#find total months
    month_count = 0
    total = 0
    previous_month = 0
    average_monthly_list = []
    greatest_increase = 0
    greatest_decrease = 99999999

    for row in csvreader:
        month_count = month_count + 1
        #print(row[1])
        total = total + int(row[1])
        current_value = int(row[1])
        monthly_change = current_value - previous_month
        previous_month = current_value 
        average_monthly_list.append(monthly_change)
        average_monthly_change = sum(average_monthly_list) / len(average_monthly_list)
        if monthly_change > greatest_increase: 
            greatest_increase = monthly_change
            greatest_increase_date = row[0]
        elif monthly_change < greatest_decrease:
            greatest_decrease = monthly_change
            greatest_decrease_date = row[0]
        
    print("Financial Analysis")
    print("___________________________")
    print("Total Months: " + str(month_count))
    print("Total: " + str(total))    
    #print("Average  Change: " + (average_monthly_list))
    print("Average  Change: "  + str(average_monthly_change))
    #print(greatest_increase)
    #print(greatest_decrease)
    print("Greatest Decrease: " + (greatest_decrease_date))
    print("Greatest Increase: " + (greatest_increase_date))
    
    


