import os
import csv

election_csv = os.path.join("..", "Resources", "election_data.csv")

#defining variable for results

Total_votes = 0
Vote_per_candidate = {}
winner = {}

#reading the first line of the csv file
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        #counting the total number of votes 
        Total_votes += 1
        #looping each row 
        if row[2] not in Vote_per_candidate:
           Vote_per_candidate[row[2]] = 1
        else: 
             Vote_per_candidate[row[2]] +=1   

#printing the results
#using max funtion on each of the 3 candidate to detemine the winner
print("Election Results")
print("-------------------------")
print(f"Total votes: " + str(Total_votes))
print("-------------------------")
for candidate, votes in Vote_per_candidate.items(): 
    print(candidate + ": " + "{:.3%}".format(votes/Total_votes) + "   ( " + str(votes) + ")")
print("--------------------------")
winner = max(Vote_per_candidate, key=Vote_per_candidate.get)     
print(f"Winner: {winner}")
print("-------------------------")

# open the output file, then write the results
f = open("pypoll_output.txt", "w")
f.write("Election Results")
f.write("-------------------------")
f.write(f"Total votes: " + str(Total_votes))
f.write("-------------------------")
for candidate, votes in Vote_per_candidate.items(): 
    f.write(candidate + ": " + "{:.3%}".format(votes/Total_votes) + "   ( " + str(votes) + ")")
f.write("-------------------------")
f.write(f"Winner: {winner}")
f.writet("-------------------------")

