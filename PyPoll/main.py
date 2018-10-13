#calling modules
import csv
import os

#initializing variables
numVotes = 0

#opening file election_data.csv and reading it
electionData = os.path.join('PyPoll', 'Resources', 'election_data.csv')
with open(electionData, 'r', newline = "") as csvfile:
    readData = csv.reader(csvfile,delimiter = ',')
    
    #excluding header
    header = next(readData)

    #iterating over whole document
    for row in readData:
        
        #adding to numVotes and totChange for total values
        numVotes += 1

#formatting output
output = (f"\nElection Results\n"
        f"---------------------------\n"
        f"Total Votes: {numVotes}\n"
        f"---------------------------\n")

#printing output
print(output)