import os

import csv

csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    
    total = 0
    id_list = []
    county_list = []
    candidates_list = []
    #previous_month = 0
    #candidates_list = []
   # percentage_of_votes = 0
    #total_votes_won = 0
    #winner = 0

    for row in csvreader:
        id_list.append(row)
        county_list.append(row[1])
        candidates_list.append(row[2])
    
    khan_votes = candidates_list.count('Khan')
    correy_votes = candidates_list.count('Correy')
    li_votes = candidates_list.count('Li')
    o_tooly_votes = candidates_list.count("O'Tooley")
    #print(o_tooly_votes)
    total_number_votes = len(id_list)
    percentage_khan = (khan_votes / total_number_votes) * 100
    percentage_correy = (correy_votes / total_number_votes) * 100
    percentage_li = (li_votes / total_number_votes) * 100
    percentage_o_tooly = (o_tooly_votes / total_number_votes) * 100

    print(f"\nElection Votes\n--------------\nTotal Votes: {total_number_votes}\n--------------\nKhan: {percentage_khan:.2f}% ({khan_votes})\nCorrey: {percentage_correy:.2f}% ({correy_votes})\nLi: {percentage_li:.2f}% ({li_votes})\nO'Tooley: {percentage_o_tooly:.2f}% ({o_tooly_votes})\n--------------\nWinner: Khan\n")
    
    
    
    
    
    #print(f'\n--------------\n')
    #print(percentage_khan)
    
    #candidates_names = []
    
                             
    #print("Election Results")
    #print("______________________")
    #print("Total Votes: " + str(total_number_votes))


        

    


