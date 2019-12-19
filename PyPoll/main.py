import os
import csv

election_csv = ("election_data.csv")


total_votes = 0
#candidate = 0
candidate_list = []
#vote_percent = []
vote_count = []


with open (election_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:

        total_votes = total_votes + 1
        candidate = row[2]

        if candidate in candidate_list:
            candidate_index = candidate_list.index(candidate)
            vote_count[candidate_index] = vote_count[candidate_index] + 1

        else:
            candidate_list.append(candidate)
            vote_count.append(1)

vote_percent = []
max_votes = vote_count[0]
max_index = 0

for x in range(len(candidate_list)):
    total_vote_percent = round(vote_count[x]/total_votes*100, 2)
    vote_percent.append(total_vote_percent)

    if vote_count[x] > max_votes:
        max_votes = vote_count[x]
        max_index = x

election_winner = candidate_list[max_index]

print("Election Results")
print("-----------------")
print(f"Total Votes: {total_votes}")
print("-----------------")
for x in range(len(candidate_list)):
    print(f"{candidate_list[x]}: {vote_percent[x]}% ({vote_count[x]})")
print("-----------------")
print(f"Winner: {election_winner}")
print("-----------------")

with open('PyPollAnalysis.txt', 'w') as text:
    text.write("Election Results" + "\n")
    text.write("-----------------\n")
    text.write(f"Total Votes: {total_votes}""\n")
    text.write("-----------------\n")
    for x in range(len(candidate_list)):
        text.write(f"{candidate_list[x]}: {vote_percent[x]}% ({vote_count[x]})""\n")
    text.write("-----------------\n")
    text.write(f"Winner: {election_winner}""\n")
    text.write("-----------------\n")