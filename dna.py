import sys
import csv



if len(sys.argv) != 3: # Program takes in 2 command line arguments, first one is the database of people and their str count, second is the dna sequence to be identified
    print("Usage: Incorrect command line inputs.")
    sys.exit(1)

str_count = [] # List of lists 
with open(sys.argv[1], "r") as file: # Opens up the CSV file containing the STR database
    reader = csv.reader(file)
    for row in reader:
        str_count.append(row)
        
str_count1 = [] # List of dictionaries
with open(sys.argv[1], "r") as file: # Opens up the CSV file containing the STR database
    reader = csv.DictReader(file)
    for row in reader:
        str_count1.append(row)

with open(sys.argv[2], "r") as file: # Opens up the txt file containing the DNA sequence to be identified
    for seq in file:
        dna_seq = seq

strs = []
for x in str_count[0]: # Appends the STR's into a list called "strs"
    if x != 'name':
        strs.append(x)

counts_str = [] # Stores the number of consequtive times a str has occured in the dna sequence
counts = {}
for i in range(len(strs)): # This loop will check to see how many times each str appears in the dna sequence consecutively.
    x = strs[i]
    z = 0  # z, y are just variables we need to iteriate through the dna sequence with proper steps
    y = 0
    counts_str.append([])
    counts[strs[i]] = [0]
    
    while y <= len(dna_seq):
        if x in dna_seq[y: y + (len(strs[i]))]:
            for j in range(y, len(dna_seq), len(strs[i])):
                if x in dna_seq[j: j + len(strs[i])]:
                    z += 1
                elif z != 0:
                    counts_str[i].append(z)
                    counts[strs[i]] = counts_str[i]
                    y = j
                    z = 0
                    break
            
                y = j
                y += 1
            
        else:
            y += 1
            
for x in counts:
    counts[x] = (sorted(counts[x], reverse = True))[0] # We sort the list of consequitive counts of strs and select the highest count number for each str

for i in range(len(str_count1)): # Compare the str counts for each person with the str counts from the dna sequence, if a complete match we return the 
    equal = 0                    # corresponding name    
    for x in str_count1[i]:
        if x != 'name':
            if int((str_count1[i])[x]) == counts[x]:
                equal += 1
    
    if equal == len(strs):
        print(f"{(str_count1[i])['name']}")
        sys.exit(0)
        
print("No match")
sys.exit(0)