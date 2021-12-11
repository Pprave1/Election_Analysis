
import csv
import os

#  Assign a variable for the file to load and the path.
file_to_load=os.path.join("D:\Priya\OsuBootCampModules\OSU Boot Camp\Module 3\Election_Analysis\Resources","election_results.csv")

#  Open the election results and read the file.
# with open function
election_data = open(file_to_load, 'r')
#with open(file_to_load) as election_data:
# Read the file object with the reader function.
file_reader = csv.reader(election_data)
#Print the header row.
headers = next(file_reader)
print(headers)
   #To do: perfrom analysis.
#print (election_data)
#Print each row in the CSV file. 
#for row in  file_reader:
#print(row)



    


 
    


# The total number of votes cast



# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4.The total number of votes each cnadiadte won 
# 5. The winner of the election based on popular vote.