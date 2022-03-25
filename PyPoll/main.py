import os
import csv
import statistics

csvpath = os.path.join("Resources","election_data.csv")

data = []
ballot_id_list = []
total_ballots = 0
candidate_list = []
most_frequent_vote = 0

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    for row in csvreader:
        data.append(row)

# title of table and total months
for a in data:
    ballot_id_list.append(a[0])
total_ballots = len(ballot_id_list)
print("Financial Analysis")
print("---------------------------")
print("Total Votes:", total_ballots)

# greatest increase and decrease
most_frequent_vote = mode(candidate_list)
print("Winner:", most_frequent_vote)

# set variable for output file
output_file = os.path.join("election_data.txt")

# open output text file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

# write header row
    writer.writerow(["Ballot ID", "County", "Candidate"])

# write in zipped rows
    writer.writerows(data)