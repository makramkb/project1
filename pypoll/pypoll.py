#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote
import os 
file_path = os.path.join('..','pypoll','Resources','election_data.csv')
import csv

with open(file_path,'r') as election:
    csv_reader = csv.reader(election,delimiter=',')
    header = next(election)
    candidates_list = []
    total_votes=0
    candidate_count = [0,0,0]
    candidate_percentagge_vote = [0,0,0]
    for row in csv_reader:
        total_votes += row.count(row[0])
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
        for i in range(len(candidates_list)):
            if candidates_list[i]==row[2]:
                candidate_count[i]+=1
        for j in range(len(candidate_count)):
            candidate_percentagge_vote[j] = round((candidate_count[j]/total_votes)*100,2)

            
    

    print(f'The total votes is {total_votes}')
    print(f'The candidates are : {candidates_list}')
    print(f'The candidates received total votes as following :{candidate_count}')
    print(f'The total percentage receive by candidate is : {candidate_percentagge_vote}')
    print(f'The winner is {candidates_list[candidate_count.index(max(candidate_count))]} with {candidate_percentagge_vote[candidate_count.index(max(candidate_count))]} %')


pypoll_analysis_path = os.path.join('..','pypoll','pypoll_analysis.txt')
with open(pypoll_analysis_path,'w') as pypoll:
    pypoll.write(f'The total votes received in this campaign is {total_votes}\n')
    pypoll.write('\n')
    pypoll.write(f'The candidates who participated are : {candidates_list}\n')
    pypoll.write('\n')
    pypoll.write(f'The votes received pre candidates are as follow : {candidate_count}\n')
    pypoll.write('\n')
    pypoll.write(f'The total percentage received per candidate is {candidate_percentagge_vote}\n')
    pypoll.write('\n')
    pypoll.write(f'The winner is {candidates_list[candidate_count.index(max(candidate_count))]} with {candidate_percentagge_vote[candidate_count.index(max(candidate_count))]} %')

