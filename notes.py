import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#NOTESSSSSSSSSS REMEMEBER:
#______________________________________________________
#Loop through rows of a data frame
#Looping through dictionaries:

for (key, value) in student_dict.items():
    #Access key and value
    pass
#########
#Dicitionary Comprehension\\
# Keyword Method with items()
# {new_key:new_value for (key, value) in dic.items()}


#______________________________________________________
student_data_frame = pandas.DataFrame(student_dict)
#
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #THEN YOU CAN access row.student or row.score
    pass
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
