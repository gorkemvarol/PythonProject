import os
import csv

Pypoll = os.path.join("Resources", "election_data.csv")


candidatelist = []
percentages = []
totalv = 0
votesnumber = []

with open(Pypoll, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        
        totalv += 1 

        
        if row[2] not in candidatelist:
            candidatelist.append(row[2])
            index = candidatelist.index(row[2])
            votesnumber.append(1)
        else:
            index = candidatelist.index(row[2])
            votesnumber[index] += 1
    
    
    for votes in votesnumber:
        percentage = (votes/totalv) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percentages.append(percentage)
    
    
    winner = max(votesnumber)
    index = votesnumber.index(winner)
    winning_candidate = candidatelist[index]


print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(totalv)}")
print("--------------------------")
for i in range(len(candidatelist)):
    print(f"{candidatelist[i]}: {str(percentages[i])} ({str(votesnumber[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")


output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(totalv)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidatelist)):
    line = str(f"{candidatelist[i]}: {str(percentages[i])} ({str(votesnumber[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))













