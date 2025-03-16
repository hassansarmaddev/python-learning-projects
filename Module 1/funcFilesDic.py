########################################readFile ########################################


# fileref = open("testfile.txt", "r")
# contents = fileref.read()
# print(contents[:100])
# fileref.close()

# fileref = open("testfile.txt", "r")
# lines = fileref.readlines()
# print(lines[:5])
# fileref.close()

# fileref = open("testfile.txt", "r")
# lines = fileref.read()
# for lin in lines[:2]:
#     print(lin)
# fileref.close()    


########################################writing text file########################################

# filename = "squared_numbers.txt"
# outfile = open(filename, "w")

# for number in range(1, 13):
#     square = number * number
#     outfile.write(str(square) + "\n")

# outfile.close()

# infile = open(filename, "r")
# print(infile.read()[:10])
# infile.close()
    
# file = open(r"C:\Users\hassa\Downloads\testfolder\squared_numbers.txt", "r")
# contents = file.readlines()
# print(contents)

########################################using with for Files########################################

# with open('testfile.txt', 'r') as md:
#     for line in md:
#         print(line)
# #continue on with other code.        
# with open('testfile.txt', 'r') as md:
#     for line in md:
#         print(line)

# fname = 'testfilesample.txt'
# with open(fname, 'w') as mkf:
#     for x in range(10):
#         mkf.write(str(x))
#         mkf.write('\n')


########################################
#reate text file and counts the frequency of each word in the file


# from collections import Counter  # Import Counter from the collections module to count occurrences of words.

# filename = "testfile.txt"  # Specify the name of the file to read.

# word_counts = Counter()  # Create an empty Counter object to store word frequencies.

# # Open the file in read mode ('r')
# with open(filename, "r") as file:
#     for line in file:  # Iterate over each line in the file
#         words = line.strip().lower().split()  
#         # .strip() removes leading and trailing whitespace (including newlines)
#         # .lower() converts all words to lowercase to ensure case insensitivity
#         # .split() splits the line into a list of words based on spaces
        
#         word_counts.update(words)  # Update the Counter with the words from the current line

# # Print the 10 most common words along with their frequencies
# print(word_counts.most_common(10))  
# # .most_common(10) retrieves the top 10 most frequent words as a list of (word, count) tuples
"""
write code to count lines and words
"""
# fname = open("emotion_words.txt", "r")
# num_lines = 0
# for line in fname:
#     num_lines += 1
# fname.close()    
# print(num_lines)  


# fname = open("emotion_words.txt", "r")
# count = 0
# for line in fname:
#     words = line.split()
#     print(words)
#     count += len(words)
#     print(count)    
# fname.close()
# print(count)    
 
