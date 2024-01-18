# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 19:22:13 2024

@author: miame
"""
###PyPoll Challenge for Module 3 Challenge###

#Importing the necessary modules/libraries
import csv

# Import Dependencies

# Specify the paths for PyBank
csv_file_path = 'Resources/budget_data.csv'
output_file_path_pybank = 'Analysis/PyBank_Analysis_Result.txt'

# Specify the path to your CSV file
csv_file_path = 'Resources/budget_data.csv'

# Create variables to serve as empty lists
Date_count = 0
total_Profit_losses = 0
value = 0
change = 0
dates = []
profits = []

#Opening and reading the CSV file
with open(csv_file_path, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #Reading and skipping the header row
    csv_header = next(csvreader)

    #Reading the first row (so that we track the changes properly)
    first_row = next(csvreader)
    Date_count += 1
    total_Profit_losses += int(first_row[1])
    value = int(first_row[1])
    
    #Going through each row of data after the header & first row 
    for row in csvreader:
        # Keeping track of the dates
        dates.append(row[0])
        
        # Calculate the change, then add it to list of changes
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #Total number of months
        Date_count += 1

        #Total net amount of "Profit/Losses over entire period"
        total_Profit_losses = total_Profit_losses + int(row[1])

    #Greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #Greatest decrease (lowest increase) in profits 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    #Average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits)/len(profits)
    
#Displaying information
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(Date_count)}")
print(f"Total am of Profit/Losses over period: ${str(total_Profit_losses)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

#Exporing to .txt file
output = open(output_file_path_pybank, "w")

line1 = "Financial Analysis:"
line2 = "----------------------------"
line3 = str(f"Total Months: {str(Date_count)}")
line4 = str(f"Total: ${str(total_Profit_losses)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))

