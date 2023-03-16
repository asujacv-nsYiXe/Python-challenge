'''***********PyBank - Financial Dataset Analysis***********
create a Python script that analyzes the records to calculate each of the following:
* The total number of months included in the dataset
* The net total amount of "Profit/Losses" over the entire period
* The changes in "Profit/Losses" over the entire period, and then the average of those changes
* The greatest increase in profits (date and amount) over the entire period
* The greatest decrease in profits (date and amount) over the entire period

---**************References**************---
---*https://docs.python.org/3/library/
---*https://docs.python.org/3/contents.html
---*https://www.w3schools.com/python/
---*https://peps.python.org/pep-0498/#how-to-specify-the-location-of-expressions-in-f-strings
'''
#import required modules
import os
import csv

#Define required variables
listDate = []               #used to store list of date values from csv data set
listProfitLoss = []         #used to store list of profitloss values from csv data set
listChangeInProfitLoss = [] #used to store list of change in profitloss - calcualted value

#get the budget csv dataset path
dataSetFilePath = os.path.join(os.getcwd(),"Resources","budget_data.csv")

#open the csv file and store the data in a reader object
with open(dataSetFilePath,'r', newline='') as budgetCsvFile:
    budgetCSVDataSet = csv.reader(budgetCsvFile,dialect = "excel", delimiter =',')
    
    #Read the header and store it in a variable - this will be ignored while creating list
    budgetFileHeader = next(budgetCSVDataSet)
    
    #Read each row from the reader and set the values to list 
    for eachRow in budgetCSVDataSet:

        listDate.append(eachRow[0])
        listProfitLoss.append(int(eachRow[1]))

#get the total number of months included in the dataset
totalMonths = len(listDate)

#get the net total amount of "Profit/Losses" over the entire period
sumOfProfitLoss = sum(listProfitLoss)

#get the changes in "Profit/Losses" over the entire period in a list
for eachPLRow in range(1, len(listProfitLoss)):
    listChangeInProfitLoss.append(listProfitLoss[eachPLRow]-listProfitLoss[eachPLRow-1])

#get the average of "Profit/Losses" changes over the entire period
avgChange = round(sum(listChangeInProfitLoss)/len(listChangeInProfitLoss),2)

#get the index of the greatest increase in profits over the entire period
indexGreatestProfitIncrease = listProfitLoss.index((max(listProfitLoss)))

#get the index of the greatest decrease in profits over the entire period
indexGreatestProfitDecrease = listProfitLoss.index((min(listProfitLoss)))

#Print the financial analysis output to terminal
print("```\nFinancial Analysis\n----------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: {sumOfProfitLoss}")
print(f"Average Change: ${avgChange}")
print(f"Greatest Increase in Profits: {listDate[indexGreatestProfitIncrease]} (${listProfitLoss[indexGreatestProfitIncrease]})")
print(f"Greatest Decrease in Profits: {listDate[indexGreatestProfitDecrease]} (${listProfitLoss[indexGreatestProfitDecrease]})")
print("```")

# create a budget analysis results file
analysisFilePath = os.path.join(os.getcwd(),"analysis","FinancialAnalysis.txt")
with open(analysisFilePath, 'w') as budgetAnalysis:
    #Write the budge financial analysis to text file
    budgetAnalysis.write("```\nFinancial Analysis\n----------------------------\n")
    budgetAnalysis.write(f"Total Months: {totalMonths}\n")
    budgetAnalysis.write(f"Total: {sumOfProfitLoss}\n")
    budgetAnalysis.write(f"Average Change: ${avgChange}\n")
    budgetAnalysis.write(f"Greatest Increase in Profits: {listDate[indexGreatestProfitIncrease]} (${listProfitLoss[indexGreatestProfitIncrease]})\n")
    budgetAnalysis.write(f"Greatest Decrease in Profits: {listDate[indexGreatestProfitDecrease]} (${listProfitLoss[indexGreatestProfitDecrease]})\n")
    budgetAnalysis.write("```")

    #close the file  
    budgetAnalysis.close