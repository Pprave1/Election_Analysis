import csv
import os

#  Assign a variable for the file to load and the path.
#file_to_load=os.path.join("D:\Priya\OsuBootCampModules\OSU Boot Camp\Module 3\Election_Analysis\Resources","election_results.csv")
#file_to_load="D:\Priya\OsuBootCampModules\OSU Boot Camp\Module 3\Election_Analysis\Resources\election_results.csv"
file_to_load=os.path.join("Resources","election_results.csv")
#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Resources\Analysis","election_analysis.txt")
 #1.Initialize a total vote counter.
total_votes = 0
#Declare candidate_options 
candidate_options = []
#Declare the empty dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0



# Open the election results and read the file.
#election_data = open(file_to_load, 'r')

# with open function
with open(file_to_load)as election_data:

#To do: perfrom analysis.
#Close the file.
#print(election_data)
#election_data.close()

# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")
#Use the open statement to open the file as a text file.
#outfile = open(file_to_save, "w")
#with open(file_to_save,"w") as txt_file:

# Write some data to the file
  #outfile.write("Hello World")
  #txt_file.write("Hello World")
  #Open the election results and read the file
   #txt_file.write("Counties in the Election\n--------------------------\n")
   #txt_file.write("Arapahoe,  ")
   #txt_file.write("Denver, ")
   #txt_file.write("Jefferson")
   # Write three counties to the file.
   #txt_file.write("\nArapahoe,Denver,Jefferson")
   #txt_file.write("\nArapahoe\nDenver\nJefferson")
# Close the file
#outfile.close()
# Read the file object with the reader function.
   file_reader = csv.reader(election_data)
#Print the header row.
   headers = next(file_reader)
   print(headers)
   
#print (election_data)
#Print each row in the CSV file. 
   for row in  file_reader:
   #Print the candidate name from each row
      candidate_name = row[2]
     # If the candidate does not match any existing candidate...
      if candidate_name not in candidate_options: 
      # Add the candidate name to the candidate list.
         candidate_options.append(candidate_name)
         #Begin tracking that candidate's vote count.
         candidate_votes[candidate_name] = 0
         ## Add a vote to that candidate's count.
      candidate_votes[candidate_name] += 1
      
     #2.Add to the total vote count
      total_votes +=1 
   #Print the total votes.

   print(total_votes)  
      # Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
   votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
   vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
   print(f"{candidate_name}: received {round(vote_percentage,1)}% of the vote.")
#To do: print out the winning candidate, vote count and percentage to
#terminal.
   print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
   if (votes > winning_count ) and (vote_percentage > winning_percentage):
      winning_count = votes 
      winning_percentage = vote_percentage
      winning_candidate =  candidate_name 
winning_candidate_summary = (
    f"--------------------------------\n"
    f"Winner : {winning_candidate}\n"
    f"winning Vote Count: { winning_count: ,}\n"
    f"Winning Percentage: {winning_percentage: .1f}%\n"
    f"---------------------------\n")
print(winning_candidate_summary)
 
    

 #print(row)
     
 #total_votes= total_votes+1
   
#Print the candidate list.
#print(candidate_options)
   #Print the candidate vote dictionary.
#print(candidate_votes)
           



    


 
    


# The total number of votes cast



# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4.The total number of votes each cnadiadte won 
# 5. The winner of the election based on popular vote.