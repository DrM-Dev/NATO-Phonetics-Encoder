#NATO Phonetics Encoder - 0.1       by      Dr.M-Dev
ver = 0.1
#_______________Imports:
import pandas
from gevent.util import print_run_info
#_______________|
from tkinter import *
#_______________|
MAIN_FONT = ("Courier", 11, "bold")
BUTTONS_FONT = ("Times New Roma", 8, "bold")


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
#----
icon_x = main_window_width / 4 - 20
icon_y = main_window_height / 4 - 150
#----
widgets_x = main_window_width / 4 - 20
widgets_y = main_window_height / 4 + 165

#------------
window = Tk()
window.title(f"NATO Phonetics Encoder {ver}")
window.minsize(main_window_width,main_window_height)
window.maxsize(main_window_width,main_window_height)
window.config(padx=20,pady=20)

#_____________________________ICON
main_canvas = Canvas(width=main_window_width/2, height=main_window_height/2)
#
icon_image = PhotoImage(file=r"images/NATO Phonetics.png")
prog_pic = main_canvas.create_image(300/2,300/2,image = icon_image)
#
main_canvas.place(x=icon_x,y=icon_y)

#_____________________________INPUT
input_label = Label(text="Enter Text Here:", font=MAIN_FONT)
input_label.place(x=widgets_x,y=widgets_y)

input_entry = Entry(width=60)
input_entry.place(x=widgets_x-30,y=widgets_y+25)


#_____________________________OUTPUT
output_y_displacement = 50
####
input_label = Label(text="Translation to NATO Phonetics:", font=MAIN_FONT)
input_label.place(x=widgets_x,y=widgets_y
                                +output_y_displacement)

input_entry = Text(width=45,height=8)
input_entry.place(x=widgets_x-30,y=widgets_y+25
                                +output_y_displacement)














#==============END:
window.mainloop()
