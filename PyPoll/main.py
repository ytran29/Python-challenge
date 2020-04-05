import os
import csv
from collections import defaultdict
filepath = os.path.join ("..", "Resources", "election_data.csv")
with open (filepath) as csvfile:
    PyPoll_data = csv.reader(csvfile, delimiter=',')
    csv_header = next (PyPoll_data)
    count = 0
    candidate_dict = defaultdict (int)
    for row in PyPoll_data:
        count = count +1
        candidate_dict [row[2]] += 1 
    print(count)
    print(candidate_dict)