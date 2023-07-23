PyPoll Challenge

Write a Python code to help a small, rural town modernize its vote-counting process. from a dataset called election_data.csv. The dataset is composed of 3 columns: "Ballot ID", "County" & "Candidate". Following steps are written to initialize the opening & reading of the csv file with the raw data provided :
1. Importing the csv file & opening it 
2. Reading the csv file data to process it 
3. Skipping reading the first row or the header row
4. Looping each row of the csv file to get specific calculations listed below 

Your task is to create a Python script that analyzes the votes and calculates each of the following values:
1. The total number of votes cast : Adding the number of rows in the "Ballot ID" column
2. A complete list of candidates who received votes : list the names of each unique candidate
3. The percentage of votes each candidate won : total number of votes received by each candidate / Total votes
4. The total number of votes each candidate won : Total number of votes each candidate received 
5. The winner of the election based on popular vote : using the max function on the total number of votes received by each of the candidate

Printing the values via "print(f)" function to print string values 
Creating an output file in the same folder by the name "output.txt" & writing the results in it

NOTE : The "f.write" section used to write the results to a new text file was taken from stackoverflow.com