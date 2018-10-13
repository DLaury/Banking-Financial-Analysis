#calling modules
import csv
import os

#initializing variables
numMonths = 0
totChange = 0
monthChangeAve = 0
monthChange = 0
aveChange = 0
profLoss = 0
highChange = 0
lowChange = 0

#opening file budget_data.csv and reading it
budgetData = os.path.join('PyBank', 'Resources', 'budget_data.csv')
with open(budgetData, 'r', newline = "") as csvfile:
    readData = csv.reader(csvfile,delimiter = ',')
    
    #excluding header
    header = next(readData)

    #iterating over whole document
    for row in readData:
        
        #adding to numMonths and totChange for total values
        numMonths += 1
        totChange += int(row[1])

        #skipping first row
        if profLoss != 0:

            #saving value for greatest changes
            monthChange = int(row[1]) - profLoss
            
            #saving value for average change
            monthChangeAve += int(row[1]) - profLoss

            #finding highest profit change and name
            if monthChange > highChange:
                highChangeName = row[0]
                highChange = monthChange
            
            #finding highest profit drop and name
            if monthChange < lowChange:
                lowChangeName = row[0]
                lowChange = monthChange

        #set profLoss to the current row for later compairson
        profLoss = int(row[1])

#calculating average and rounding the number to two decimal places
aveChange = round(monthChangeAve / numMonths, 2)

#formatting output
output =(f"\nFinancial Analysis \n"
        f"------------------------- \n"
        f"Total Months: {numMonths} \n"
        f"Total: ${totChange} \n"
        f"Average Change: ${aveChange} \n"
        f"Greatest Increase in Profits: {highChangeName} (${highChange}) \n"
        f"Greatest Decrease in Profits: {lowChangeName} (${lowChange})")

#printing output
print(output)

#writing output to text file
with open(os.path.join('PyBank', 'Output', 'financial_analysis.txt'), 'w') as txtfile:
    txtfile.write(output)