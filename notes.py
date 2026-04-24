#NATO Phonetics Encoder - 0.1       by      Dr.M-Dev
ver = 0.1
#_______________Imports:
import time
import pandas
from gevent.util import print_run_info
#_______________|
from tkinter import *


#========================Data-Base SETUP
nato_phonetics_DF = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_phonetics_DF)

#====================================================================================DB to DIC
nato_phonetics_DIC = { letter:meaning_column.code for (letter,meaning_column) in nato_phonetics_DF.iterrows() }
# print(nato_phonetics_DIC)            #\_____to devs wanting to lean from this:
#                                          #\___MY SOLUTION WAS SIMPLE! :)
# for (index,row) in nato_phonetics_DF:         #in short, I'm taking all the letters from the letter column..no problem
#     print(row.code)                           #the issue starts when you take the meaning, it will give you the WHOLE-ROW!!!
                                                #but thanks to the iterrows(), I was able to GET DIRECTLY TO THE VALUE which was "code"

#NOW NATO-PHONETICS-LETTERS:
nato_letters_DIC =  { index:letter_column.letter for (index,letter_column) in nato_phonetics_DF.iterrows() }
# print(nato_letters_DIC)



#OR alternatively, you can write:
FINAL_FINAL_nato_letters_DIC = { column_info.letter:column_info.code for (index,column_info) in nato_phonetics_DF.iterrows()}


#====================================================================================
# NOW TIME TO COMBINE THEM INTO 1 DIC!! using a detailed FOR-LOOP
final_NATO_ALPAHBET_DIC = { }
n = 0
#
for (index,letter) in nato_letters_DIC.items(): #<---------this can be replaced by "range()"
    # final_NATO_ALPAHBET_DIC[ f"{nato_letters_DIC[n][n]}" ] = nato_phonetics_DIC[n][n]
    letter_meaning = nato_phonetics_DIC[n]
    letter_item = nato_letters_DIC[n]
    #----------------------------------
    #debug:
    # print(letter_item)
    # print(letter_meaning)
    #
    final_NATO_ALPAHBET_DIC[f"{letter_item}"] = letter_meaning
    #########3#
    n += 1

#-------------------#-------------------#-------------------#-------------------
#my edit on the dic:
#just wanted to add SPACE as - inside the Dictionary\\
#
# <!> SUPER IMPORTANT NOTE <!>
# if you want to add a new KEY to a DIC, you MUST NOT USE .append() or .extend() like with lists
# instead, just PRETEND THAT THE KEY IS THERE!!!
#
final_NATO_ALPAHBET_DIC[" "] = '__'
final_NATO_ALPAHBET_DIC["\n"] = '|'
#as you can see, you pretend that THERE WAS " " KEY, and it equals to the value = "-"
#so..just like editing a value!

# #DEBUG
print("\n" * 5)
print(final_NATO_ALPAHBET_DIC)


#====================================================================================
transmitting = True

while transmitting:
    user_input = input("\n\nInput anything to convert it into NATO-Phonetics System\nWrite [END] to end translation-session").upper()
    #
    if user_input == "END":
        print("\nExiting Code...")
        transmitting = False
    else:
        input_letters = list(user_input)
        #debug
        print(f"\n {input_letters}")
        #
        print("Translating...")
        time.sleep(1)
        final_translation =""
        #----------------------------Translater:
        for letter in input_letters:
            letter = f"[{final_NATO_ALPAHBET_DIC[letter]}]"
            #
            final_translation += letter
        #----------------------------
        print(final_translation)














# NOTES
# =======================================================================================================================

# import pandas
#
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #NOTESSSSSSSSSS REMEMEBER:
#______________________________________________________
#Loop through rows of a data frame
#Looping through dictionaries:

# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
# #########
#Dicitionary Comprehension\\
# Keyword Method with items()
# {new_key:new_value for (key, value) in dic.items()}


#______________________________________________________
# student_data_frame = pandas.DataFrame(student_dict)
# #
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #THEN YOU CAN access row.student or row.score
#     pass
#########
#DataFrame Comprehension\\
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


#______________________________________________________
#TRUTH NUKE OF THE CENTURY
#HOLYYY MOLYYYYYYYYYYYYY

#turnsout that you can CALL FOR MORE THAN ONE ROW!!!!!!!!!!!! when you call for (index, row) in iter-rows() method of the DataFrame!!!
#BECAUASE
#as soon as you call rows..you can now use anyyyyyy row by name!! so you have access to every data in the database!!!
#JUST LIKE WHEN YOU DO LIST-COMPREHENSION WITH 'DICTIONARIES' that needs items() to work xP
# EXAMPLE:
# |
# |
#getting the CSV-DataFrame
nato_phonetics_DF = pandas.read_csv("nato_phonetic_alphabet.csv")
# now
# we want to comprehend it into a dictionary:
nato_phonetics_DIC = { }
#
#DOING THE Data-Frame Comprehension into Dictionary with .iterrows()
# -----------------------------------> nato_phonetics_DIC = { index:row for (index,row) in nato_phonetics_DF.iterrows() }
#NOW
#TIME TO ACCESS ALL ROWS..no need to mention index:row, for (index,row) just use this:
nato_phonetics_DIC = { row.letter : row.code for (index,row) in nato_phonetics_DF.iterrows()  }
#########################
print(nato_phonetics_DIC)



#=========================================================================================================
#OR just use the EXPANDED FOR-LOOP!! to get ALL THE ROWS!!!:
#
nato_phonetics_DIC.clear()
#
for (index,row) in nato_phonetics_DF.iterrows():
    letter = row.letter
    meaning = row.code
    #
    nato_phonetics_DIC[letter] = meaning
#########################
print(nato_phonetics_DIC)

############NOTE\\\\\\\\\\\\\\\\\\   Data-Frame   ->  Dictionary  ->  List  {The Comprehension Pathway} xP
############NOTE\\\\\\\\\\\\\\\\\\   Data-Frame   ->  Dictionary  ->  List  {The Comprehension Pathway} xP
############NOTE\\\\\\\\\\\\\\\\\\   Data-Frame   ->  Dictionary  ->  List  {The Comprehension Pathway} xP
############NOTE\\\\\\\\\\\\\\\\\\   Data-Frame   ->  Dictionary  ->  List  {The Comprehension Pathway} xP
############NOTE\\\\\\\\\\\\\\\\\\   Data-Frame   ->  Dictionary  ->  List  {The Comprehension Pathway} xP
############NOTE\\\\\\\\\\\\\\\\\\   Data-Frame   ->  Dictionary  ->  List  {The Comprehension Pathway} xP
