#Welcome to the Frequency Analysis App

# You are responsible for writing a program that will analyse the letter distribution of a given text. 
# Your program will take any text, remove all non-alpha characters, count the frequency of each letter 
# within the text, calculate the percentage of occurrence for each letter, and create a list of letters 
# ordered from highest occurrence to lowest occurrence. Your program will perform these operations for 
# two different bodies of text.

from collections import Counter

#Display welcome message
print("Welcome to the Word Frequency Analysis App")

#Define a list of common non-alphabet and punctuation marks
non_letters = [" ", "!", ",", "?", ";", "@", "'", "'", '"', '!', '#', '$', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

#Get user input for phrase 1
phrase_1 = input("Enter a word or phrase to count the occurence of each letter: ").lower().strip()

#Removing all non letters from phrase 1
for non_letter in non_letters:
  phrase_1 = phrase_1.replace(non_letter,"")

total_occurences = len(phrase_1)

#Create a counter object to calculate the occurence of each letter
letter_count = Counter(phrase_1)

# An alternative way to calculate the occurrence of each letter without using Counter
# letter_count = {}
# phrase_list = list(phrase_1)
# for letter in phrase_list:
#   if letter in letter_count.keys():
#     letter_count[letter] += 1
#   else:
#     letter_count[letter] = 1

print("\nHere is the frequency analysis from phrase 1:")
print("\n\tLetter\t\tOccurrence\tPercentage")
for k,v in letter_count.items():
  percentage = round((100*v) / total_occurences, 2)
  print("\t" + k + "\t\t" + str(v) + "\t\t" + str(percentage))



