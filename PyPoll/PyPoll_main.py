# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 22:17:11 2024

@author: miame
"""

#PyPoll Challenge for Module 3 Challenge

# Importing the necessary modules/libraries
import csv

# Specify the paths for PyPoll
csv_file_path_pypoll = 'Resources/election_data.csv'
output_file_path_pypoll = 'Analysis/PyPoll_Analysis_Result.txt'

# Open the CSV file and skip the header row
with open(csv_file_path_pypoll, newline='') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)  # Skip the header row

    # Create a list from the remaining rows
    election_data = list(reader)

# Calculate total votes and initialize vote counts for each candidate
total_votes = len(election_data)
charles_votes = 0
diane_votes = 0
raymon_votes = 0

# Iterate through the data to count votes for each candidate
for i in range(len(election_data)):
    if election_data[i][2] == "Charles Casper Stockham":
        charles_votes += 1
    elif election_data[i][2] == "Diana DeGette":
        diane_votes += 1
    elif election_data[i][2] == "Raymon Anthony Doane":
        raymon_votes += 1

# Calculate the percentage of votes for each candidate
charles_percent = (charles_votes / total_votes) * 100
diane_percent = (diane_votes / total_votes) * 100
raymon_percent = (raymon_votes / total_votes) * 100

# Determine the winner based on the candidate with the most votes
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
winner = max(candidates, key=lambda x: locals().get(x, 0))

# Print the results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_votes})")
print(f"Diana DeGette: {diane_percent:.3f}% ({diane_votes})")
print(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the results to a text file
with open(output_file_path_pypoll, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_votes})\n")
    output_file.write(f"Diana DeGette: {diane_percent:.3f}% ({diane_votes})\n")
    output_file.write(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_votes})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")
    