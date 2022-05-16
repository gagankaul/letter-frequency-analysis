#Welcome to the Frequency Analysis App

from collections import Counter

#Display welcome message
print("Welcome to the Word Frequency Analysis App")

#Define a list of common non-alphabet and punctuation marks
non_letters = [" ", "!", ",", "?", ";", "@", "'", "'", '"', '!', '#', '$', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def frequency_analysis(phrase_1):
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

  #Calculating the frequency of letter occurrence for the phrase
  print("\nHere is the frequency analysis for the phrase:")
  print("\n\tLetter\t\tOccurrence\tPercentage")
  for k,v in sorted(letter_count.items()):
    percentage = round((100*v) / total_occurences, 2)
    print("\t" + k + "\t\t" + str(v) + "\t\t" + str(percentage) + "%")

  #Make a list of letters from highest occurrence to lowest
  ordered_letter_count = letter_count.most_common()
  phrase_1_ordered_letters = []
  for each in ordered_letter_count:
    phrase_1_ordered_letters.append(each[0])

  #Print the list
  print("Letters in descending order of occurrence: ", end = "")
  for each in phrase_1_ordered_letters:
    print(each + " ", end = "")

#Initialize user choice as True for running the program
choice = True

#The main program loop
while choice == True:
  #Get user input for phrase 1
  sentence = input("\nEnter a word or phrase to count the occurence of each letter: ").lower().strip()
  #Run the function
  frequency_analysis(sentence)
  usr_input = input("\nWould you like to generate a frequency table for another phrase (y/n)? ").lower().strip()
  if usr_input == "n":
    choice = False