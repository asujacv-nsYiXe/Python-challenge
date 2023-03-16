'''***********PyPoll - Modernize Vote Counting Process***********
create a Python script that analyzes the votes and calculates each of the following:
* The total number of votes cast
* A complete list of candidates who received votes
* The percentage of votes each candidate won
* The total number of votes each candidate won
* The winner of the election based on popular vote.

---**************References**************---
---*https://docs.python.org/3/library/
---*https://docs.python.org/3/contents.html
---*https://www.w3schools.com/python/
---*https://peps.python.org/pep-0498/#how-to-specify-the-location-of-expressions-in-f-strings
'''
#import required modules
import os
import csv

#Define required variables
listCandiateName = []       #used to store all candicate names from the dataset
listBallotId = []           #used to store all ballotID from the dataset
winnerCandidateCount = 0    #used to store winner candidate vote count
winnderCandidateName = ""   #used to store winner candidate name
candidatePercent = 0 #used to store total number of votes each candidate won
candidateTotal = 0   #used to store percentage of votes each candidate won

#get the election result csv dataset path
electionDataPath = os.path.join(os.getcwd(),"Resources","election_data.csv")

#open the csv file and store the data in a reader object
with open(electionDataPath,'r') as electiondataCsv:
    readElectiondata = csv.reader(electiondataCsv,dialect ="excel", delimiter = ",")

    #Read the header and store it in a variable - this will be ignored while creating list
    readElectiondataHeader = next(readElectiondata)
    
    #Read each row from the reader and set the values to list 
    for eachData in readElectiondata:
        listBallotId.append(eachData[0])
        listCandiateName.append(eachData[2])

#Create a unique sorted set of candidate name
setCandidate = sorted(set(listCandiateName))

# print the a election analysis total vote results to the terminal
print("```\nElection Results\n-------------------------")
print(f'Total Votes: {len(listBallotId)}')
print("-------------------------")

# create a election analysis results file
electionAnalysisPath = os.path.join(os.getcwd(),'analysis',"ElectionAnalysis.txt")
with open(electionAnalysisPath,'w') as ElectionAnlaysisResultFile:

    # write the a election analysis total vote results to the text file
    ElectionAnlaysisResultFile.write("```\nElection Results\n-------------------------\n")
    ElectionAnlaysisResultFile.write(f'Total Votes: {len(listBallotId)}\n')
    ElectionAnlaysisResultFile.write("-------------------------\n")

    #Calculate the total number and percentage of votes each candidate won and find winner candiate
    for eachCandidate in setCandidate:
        candidatePercent = 0
        candidateTotal = 0
        candidateTotal = listCandiateName.count(eachCandidate) # Calculates total vote that each candiate won
        candidatePercent = candidateTotal/len(listCandiateName) # Calculates percentage of vote that each candiate won

        #Print each candidate's total vote count and percentatge vote to terminal
        print(f'{eachCandidate}: {"{:.3%}".format(candidatePercent)} ({candidateTotal})')
        #write the values to the text file 
        ElectionAnlaysisResultFile.write(f'{eachCandidate}: {"{:.3%}".format(candidatePercent)} ({candidateTotal})\n')

        #Write each candidate's total vote count and percentatge vote to a text file
        if candidateTotal > winnerCandidateCount:
            winnerCandidateCount = candidateTotal
            winnderCandidateName = eachCandidate

    #Print the winner candiate results to the terminal
    print("-------------------------")
    print(f'Winner: {winnderCandidateName}')
    print("-------------------------\n```")
    #write the winner candiate results to the text file
    ElectionAnlaysisResultFile.write("-------------------------\n")
    ElectionAnlaysisResultFile.write(f'Winner: {winnderCandidateName}\n')
    ElectionAnlaysisResultFile.write("-------------------------\n```")
 
    #close the file   
    ElectionAnlaysisResultFile.close