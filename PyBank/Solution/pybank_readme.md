PyBank Challenge

Write a Python code to analyze the financial records of your company from a dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses". Following steps are written to initialize the opening & reading of the csv file with raw data provided :
1. Importing the csv file & opening it 
2. Reading the csv file data to process it 
3. Skipping reading the first row or the header row
4. Looping each row of the csv file to get specific calculations listed below 

We need to calculate the following values from the data set provided:
1. The total number of months included in the dataset : for this we need to set a variable "Total_months" to count total number of monthts in the "Date" row 
2. The net total amount of "Profit/Losses" over the entire period : for this calculation first we need sum the total of values in column "Profit/Losses" if the value is positive we will add them, if value is negative we need to substratct it. This will give us the value of " Total_profit_loss"
3. The changes in "Profit/Losses" over the entire period, and then the average of those changes : Average change is calculated by dividing the value of "Total_profit_loss" / "Total_month"
4. The greatest increase in profits (date and amount) over the entire period : this can be calculated by simply using the "max" function in python on the "Profit_loss_changes" which will give us the highest value in that row
5. The greatest decrease in profits (date and amount) over the entire period : this can be calculated by simply using the "min" function in python on the "Profit_loss_changes" which will give us the lowest value in that row

Printing the values via "print(f)" function to print string values 
Creating an output file in the same folder by the name "output.txt" & writing the results in it

NOTE : The "f.write" section used to write the results to a new text file was taken from stackoverflow.com