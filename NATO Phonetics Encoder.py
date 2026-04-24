#NATO Phonetics Encoder - 0.1       by      Dr.M-Dev
ver = 0.1
#_______________Imports:
import pandas
from gevent.util import print_run_info
#_______________|
import string
from tkinter import *
#_______________|
MAIN_FONT = ("Courier", 11, "bold")
BUTTONS_FONT = ("Times New Roma", 12, "bold")


print('''                                                                                                                                                  
                                                              ...::::.      ...::::::::    :.      .:.   
  5@@@@@@@@B!    &@@@@@@@&G:        ^G&@@@&P#@@@@B~          J@@@@@@@@@G.   #@@@@@@@@@@   .@@B    7@@?   
  G@@~::::J@@!   @@#     B@@.      :@@G::~&@@!::Y@@~         J@@~    ^@@B   #@@.           !@@J  .@@B    
  G@@     .@@Y   @@@    5&@#       ~@@!   B@&   :@@?         J@@:     &@#   #@@BBBBBBB      P@@: #@@.    
  7BP     .@@J   PBGGGGGB@@B       :BB^   B@&   :@@?         ~GP.     &@#   JGPYYYYYYY       &@# @@!     
  Y&&^....?@@7   #&P     J@@:  ##  ^&&~   B@&   ^@@?         ?@@7:  :7@@P   Y@& ......       ^@@@@P      
  P@@@@@@@@&?    &@B     ?@@:  ##  ~@@!   B@&   :@@?         ?@@@@@@@@#J    J&@@@@@@@@?       ?@@B  


                                                             !J!:                                                                
                                                              ^G@@&P7:                                                           
                                         .~7YGB#&&&&&&&#BG5?~:  .Y@@@@&G^                                                        
                                    :?P&@@@@@@@@@@@@@@@@@@@@@@@&G?J@@@@@&                                                        
                                .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P   ...                                                 
                              ~B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BG&&@@@@                                              
                            ?&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                                             
                          7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#GYP#&J                                            
                        .B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!                                                
                       :&@@@@@@@@@@@@@@@@J7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P                                               
                      .@@@@@@@@@@@@@@@@#:  ^&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G                                              
                      #@@@@@@@@@@@@@@&7      P@@@@@@@@@@@@@B&@@@@@@@&@@#&@@@@@@@@@@J                                             
                     !@@@@@@@@@@@@@&?         ^#@@@@&&@@@@@@#PPGB##? B@5#@#@@@@@@@@@:                                            
                     B@@@@@@@@@@@G~             ^B@@@&GG#@@@@@@@#~   .&#J@Y&@@@@@@@@G                                            
                     @@@@@@@@@@~                  .?#@@@&BGPGBBJ      .#5G&J@@@@@@@@@.                                           
                   .@@@@@@@@@7      !PB##B4^        .^JG#&&P:  ^4B###P4?!~!?@@@@@@@@^                                           
                   .@@@@@@@@#      !4~.. .~4^                 ~4~....~4^    #@@@@@@@^   .~                                      
               ~BJ :@@@@@@@@BJYYYYYYJJJJYJJJJJJJ?!.     .!?JYYYJJYYYJJJYYYYY&@@@@@@@P7: .G#?.                                   
            .?BG^  &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?...5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?  .Y#5:                                 
          :5BJ.    @@@@@@@@@&PJJJJJJ????JJJJ5&@@@@@@@@@@@@@@@GYJJ??????JJJJJYB@@@@@@@@@Y     7BB~                               
        !GG~       .YGG@@@@B        ...       G@@@@@@@@@@@@@:     .::.        !@@@@&GP7        ^G#?                             
     .JB5:             &@@@Y      4P..P@G.    7@@@@@@@@@@@@&    ^:^B@@@P.      @@@@~             .J#5.                          
     J@J               &@@@5     G@@4Y&@@&    ?@@@@?::^#@@@&   ~@4^B@@@@#     .@@@@~              ^#&:                          
      .5#J.            &@@@5     ?@@@@@@@P    7@@@@.   ?@@@&   .@@@@@@@@Y     .@@@@~           .J#P:                            
        .?#P:          #@@@G      .JGBBY:     5@@@&    ^@@@@.    ?B&&#P^      :@@@@~         ^PBJ.                              
           ~BB!        7@@@@5.              :P@@@@J     #@@@&!.             .!&@@@&        7BG~                                 
             :5#J.      ?@@@@@@@@@@@@@@@@@@@@@@@@J      .#@@@@@@&&&&&&&@&&@@@@@@@B.     :5BY.                                   
               .J#!      .7G&&@@@@@@@@@@@@@@&&G7.         ^5#&@@@@@@@@@@@@@@@&BJ:       7!                                      


 ''')

print(f"******** WELCOME TO NATO Phonetics Encode {ver}    -   By: Dr.m DEV *********")

#==========================================================================================================
#==========================================================================================================
#==========================================================================================================
#==========================================================================================================

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
# normal English alphabet
alphabet = list(string.ascii_lowercase) # Output: ['a', 'b', 'c', ..., 'z']
# modify it to fit the all caps NATO-Phonetics
final_alphabet = [letter.upper() for letter in alphabet]
#
#-------------------
#
# adding numbers & symbols
numbers_symbols_list = [0,1,2,3,4,5,6,7,8,9]
# turning int to str
numbers_symbols_list = [str(number) for number in numbers_symbols_list]
#
# This contains: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
symbols_list = list(string.punctuation)
#
numbers_symbols_list.extend(symbols_list)

# #DEBUG
# print("\n" * 5)
# print(final_NATO_ALPAHBET_DIC)
# print(alphabet)
# print(final_alphabet)
# print(numbers_symbols_list)


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
main_canvas = Canvas(width=main_window_width, height=main_window_height/2)
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
output_label = Label(text="Translation to NATO Phonetics:", font=MAIN_FONT)
output_label.place(x=widgets_x,y=widgets_y
                                +output_y_displacement)

output_entry = Text(width=45,height=8)
output_entry.place(x=widgets_x-30,y=widgets_y+25
                                +output_y_displacement)


#____________________Translation\\
trans_button_dis = 100

def translate():
    global final_NATO_ALPAHBET_DIC
    global final_alphabet
    global numbers_symbols_list
    #####
    user_input = (str(input_entry.get())).upper()
    user_input_listed = list(user_input)
    #----
    output = ""
    #####

    #----------------clear text-box
    output_entry.delete("1.0", END)

    #----------------Translation
    for character in user_input_listed:
        if character in final_alphabet:
            output += final_NATO_ALPAHBET_DIC[character]
            output += "."
        elif character in numbers_symbols_list:
            output += character
            output += "."
        else:
            output += character
            output += "."
    #-------#
    output_entry.insert(END, f"{output}")

#@==============================================
translate_button = Button(text="Translate", font=BUTTONS_FONT, width=8,height=1, command=translate, bg="dodgerblue", fg="white")
translate_button.place(x=widgets_x+100,y=widgets_y+120
                                +trans_button_dis)
#-----other methods of activation:
translate_button.focus() #activate with the space-bar
#
window.bind('<Return>', lambda event: translate_button.invoke()) #activate with Return-key "Enter"

#==============END:
window.mainloop()
