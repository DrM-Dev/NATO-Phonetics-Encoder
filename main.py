#_______________Imports:
import time
import pandas
from gevent.util import print_run_info

#_______________Setup:
nato_phonetics_DF = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_phonetics_DF)
#Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
#DON'T USE data_frame_name.dic()
#because it won't give you the same result as in : {"A": "Alfa", "B": "Bravo"}



#====================================================================================
nato_phonetics_DIC = { letter:meaning.code for (letter,meaning) in nato_phonetics_DF.iterrows() }
# print(nato_phonetics_DIC)            #\_____
#                                          #\___MY SOLUTION WAS SIMPLE! :)
# for (index,row) in nato_phonetics_DF:         #in short, I'm taking all the letters from the letter column..no problem
#     print(row.code)                           #the issue starts when you take the meaning, it will give you the WHOLE-ROW!!!
                                                #but thanks to the iterrows(), I was able to GET DIRECTLY TO THE VALUE which was "code"

print("\n"*10)
#NOW NATO-PHONETICS-LETTERS:
nato_letters_DIC =  { index:column.letter for (index,column) in nato_phonetics_DF.iterrows() }
# print(nato_letters_DIC)


# NOW TIME TO COMBINE THEM INTO 1 DIC!! using a detailed FOR-LOOP
final_NATO_ALPAHBET_DIC = { }
n = 0
#
for (index,letter) in nato_letters_DIC.items(): #<---------this can be replaced by "range()"
    # final_NATO_ALPAHBET_DIC[ f"{nato_letters_DIC[n][n]}" ] = nato_phonetics_DIC[n][n]
    letter_item = nato_letters_DIC[n]
    letter_meaning = nato_phonetics_DIC[n]
    # ))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
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
