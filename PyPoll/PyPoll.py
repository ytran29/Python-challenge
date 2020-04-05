import os
import csv
filepath = os.path.join ("..", "Resources", "election_data.csv")
with open (filepath) as csvfile:
    PyPoll_data = csv.reader(csvfile, delimiter=',')
    csv_header = next (PyPoll_data)
    count = 0
    candidate_dict = {}
    for row in PyPoll_data:
        count = count +1
        if row[2] not in candidate_dict:
            candidate_dict [row[2]] = 1
        else:       
            candidate_dict [row[2]] += 1
    print(candidate_dict)
    max_votecounts = max (candidate_dict.values())
    for k,v in candidate_dict.items():
        if v == max_votecounts:
            winner = k
    print(f"the winner is {winner}")
