#NATO Phonetics Encoder - 0.1       by      Dr.M-Dev
ver = 0.1
#_______________Imports:
import pandas
from gevent.util import print_run_info
#_______________|
from tkinter import *


#========================Data-Base SETUP
nato_phonetics_DF = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_phonetics_DF)

#====================================================================================DB to DIC
#Turning Database into Dictionary:
final_NATO_ALPAHBET_DIC = { column_info.letter:column_info.code for (index,column_info) in nato_phonetics_DF.iterrows()}
#-------------------
#my edit on the dic:
#just wanted to add SPACE as - inside the Dictionary\\
final_NATO_ALPAHBET_DIC[" "] = '__'
final_NATO_ALPAHBET_DIC["\n"] = '|'


# #DEBUG
print("\n" * 5)
print(final_NATO_ALPAHBET_DIC)




#==================================================================UI-Setup:
window = Tk()
window.title(f"NATO Phonetics Encoder{ver}")
window.maxsize(600,600)
window.maxsize(600,600)

