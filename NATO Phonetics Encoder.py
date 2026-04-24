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
final_NATO_ALPAHBET_DIC = { row_info.letter:row_info.code for (index,row_info) in nato_phonetics_DF.iterrows()}
#-------------------
#my edit on the dic:
#just wanted to add SPACE as - inside the Dictionary\\
final_NATO_ALPAHBET_DIC[" "] = '__'
final_NATO_ALPAHBET_DIC["\n"] = '|'
#
# adding numbers
numbers_list = [0,1,2,3,4,5,6,7,8,9]

# #DEBUG
print("\n" * 5)
print(final_NATO_ALPAHBET_DIC)


#==================================================================UI-Setup:
# dimensions
main_window_width = 600
main_window_height = 600
#
widgets_x = main_window_width / 4 - 20
widgets_y = main_window_height / 4

#------------
window = Tk()
window.title(f"NATO Phonetics Encoder {ver}")
window.minsize(main_window_width,main_window_height)
window.maxsize(main_window_width,main_window_height)
window.config(padx=20,pady=20)

#_____________________________ICON
canvas = Canvas(width=main_window_width/2, height=main_window_height/2, background="black")
canvas.place(x=widgets_x,y=widgets_y-150)

#_____________________________INPUT
input_label = Label(text="Enter Text Here")
input_label.place(x=widgets_x,y=widgets_y)

#_____________________________OUTPUT















#==============END:
window.mainloop()
