import csv
import os

#  Assign a variable for the file to load and the path.
#file_to_load=os.path.join("D:\Priya\OsuBootCampModules\OSU Boot Camp\Module 3\Election_Analysis\Resources","election_results.csv")
#file_to_load="D:\Priya\OsuBootCampModules\OSU Boot Camp\Module 3\Election_Analysis\Resources\election_results.csv"
file_to_load=os.path.join("Resources","election_results.csv")
#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Resources\Analysis","election_analysis.txt")
 
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
   #for row in  file_reader:
     # print(row)



    


 
    


# The total number of votes cast



# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4.The total number of votes each cnadiadte won 
# 5. The winner of the election based on popular vote.