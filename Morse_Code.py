'''
# Purpose: Change inputed words into Morse Code and Changes inputed Morse Code into words
# 
# @author Harry Cogdill
# @version June 30, 2019
# 
'''

Translate_Words_To_Morse_Code = input("Please enter your choice of words: ")
Change_25 = Translate_Words_To_Morse_Code.replace( " " , "" )
Change_24 = Change_25.replace( "A" , "a")
Change_23 = Change_24.replace( "B" , "b")
Change_22 = Change_23.replace( "C" , "c")
Change_21 = Change_22.replace( "D" , "d")
Change_20 = Change_21.replace( "E" , "e")
Change_19 = Change_20.replace( "F" , "f")
Change_18 = Change_19.replace( "G" , "g")
Change_17 = Change_18.replace( "H" , "h")
Change_16 = Change_17.replace( "I" , "i")
Change_15 = Change_16.replace( "J" , "j")
Change_14 = Change_15.replace( "K" , "k")
Change_13 = Change_14.replace( "L" , "l")
Change_12 = Change_13.replace( "M" , "m")
Change_11 = Change_12.replace( "N" , "n")
Change_10 = Change_11.replace( "O" , "o")
Change_9 = Change_10.replace( "P" , "p")
Change_8 = Change_9.replace( "Q" , "q")
Change_7 = Change_8.replace( "R" , "r")
Change_6 = Change_7.replace( "S" , "s")
Change_5 = Change_6.replace( "T" , "t")
Change_4 = Change_5.replace( "U" , "u")
Change_3 = Change_4.replace( "V" , "v")
Change_2 = Change_3.replace( "W" , "w")
Change_1 = Change_2.replace( "X" , "x")
Change0 = Change_1.replace( "Y" , "y")
Change1 = Change0.replace( "Z" , "z")
Change2 = Change1.replace( "a" , "•_  ")
Change3 = Change2.replace( "b" , "_•••  ")
Change4 = Change3.replace( "c" , "_•_•  ")
Change5 = Change4.replace( "d" , "_••  ")
Change6 = Change5.replace( "e" , "•  ")
Change7 = Change6.replace( "f" , "••_•  ")
Change8 = Change7.replace( "g" , "_ _•  ")
Change9 = Change8.replace( "h" , "••••  ")
Change10 = Change9.replace( "i" , "••  ")
Change11 = Change10.replace( "j" , "•_ _ _  ")
Change12 = Change11.replace( "k" , "_•_  ")
Change13 = Change12.replace( "l" , "•_••  ")
Change14 = Change13.replace( "m" , "_ _  ")
Change15 = Change14.replace( "n" , "_•  ")
Change16 = Change15.replace( "o" , "_ _ _  ")
Change17 = Change16.replace( "p" , "•_ _•  ")
Change18 = Change17.replace( "q" , "_ _•_  ")
Change19 = Change18.replace( "r" , "•_•  ")
Change20 = Change19.replace( "s" , "•••  ")
Change21 = Change20.replace( "t" , "_  ")
Change22 = Change21.replace( "u" , "••_  ")
Change23 = Change22.replace( "v" , "•••_  ")
Change24 = Change23.replace( "w" , "•_ _  ")
Change25 = Change24.replace( "x" , "_••_  ")
Change26 = Change25.replace( "y" , "_•_ _  ")
Change27 = Change26.replace( "z" , "_ _••  ")
Change28 = Change27.replace( "1" , "•_ _ _ _  ")
Change29 = Change28.replace( "2" , "••_ _ _  ")
Change30 = Change29.replace( "3" , "•••_ _  ")
Change31 = Change30.replace( "4" , "••••_  ")
Change32 = Change31.replace( "5" , "•••••  ")
Change33 = Change32.replace( "6" , "_••••  ")
Change34 = Change33.replace( "7" , "_ _•••  ")
Change35 = Change34.replace( "8" , "_ _ _••  ")
Change36 = Change35.replace( "9" , "_ _ _ _•  ")
Change37 = Change36.replace( "0" , "_ _ _ _ _  ")
print("Your Message Translated into Morse Code: " + Change37)

Continue = input("Do you want to translate something from Morse Code into English? [y/n]\n")

if Continue == "y":
	Translate_Morse_Code_To_Words = input("Please enter your choice of Morse Code (for each space use two spaces and make a space in between each underscore): ")
if Continue == "n":
	exit()

Translate1 = Translate_Morse_Code_To_Words
Translate2 = Translate1.replace( "_ _ _ _ _  " , "0")
Translate3 = Translate2.replace( "•_ _ _ _  " , "1")
Translate4 = Translate3.replace( "_ _ _ _•  " , "9")
Translate5 = Translate4.replace( "••_ _ _  " , "2")
Translate6 = Translate5.replace( "_ _ _••  " , "8")
Translate7 = Translate6.replace( "•_ _ _  " , "j" )
Translate8 = Translate7.replace( "_ _••  " , "z" )
Translate9 = Translate8.replace( "•••_ _  " , "3")
Translate10 = Translate9.replace( "_ _•••  " , "7")
Translate11 = Translate10.replace( "•_ _•  " , "p" )
Translate12 = Translate11.replace( "_ _•_  " , "q" )
Translate13 = Translate12.replace( "_•_ _  " , "y" )
Translate14 = Translate13.replace( "_ _ _  " , "o" )
Translate15 = Translate14.replace( "•••_  " , "v" )
Translate16 = Translate15.replace( "•••••  " , "5")
Translate17 = Translate16.replace( "••••_  " , "4")
Translate18 = Translate17.replace( "_••••  " , "6")
Translate19 = Translate18.replace( "••••  " , "h" )
Translate20 = Translate19.replace( "_•••  " , "b" )
Translate21 = Translate20.replace( "_•_•  " , "c" )
Translate22 = Translate21.replace( "••_•  " , "f" )
Translate23 = Translate22.replace( "•_••  " , "l" )
Translate24 = Translate23.replace( "•_ _  " , "w" )
Translate25 = Translate24.replace( "_ _•  " , "g" )
Translate26 = Translate25.replace( "_••_  " , "x" )
Translate27 = Translate26.replace( "•_•  " , "r" )
Translate28 = Translate27.replace( "•••  " , "s" )
Translate29 = Translate28.replace( "_••  " , "d" )
Translate30 = Translate29.replace( "_•_  " , "k" )
Translate31 = Translate30.replace( "••_  " , "u" )
Translate32 = Translate31.replace( "_ _  " , "m" )
Translate33 = Translate32.replace( "••  " , "i" )
Translate34 = Translate33.replace( "•_  " , "a" )
Translate35 = Translate34.replace( "_•  " , "n" )
Translate36 = Translate35.replace( "_  " , "t" )
Translate37 = Translate36.replace( "•  " , "e" )
print("Your Message Translated into English: " + Translate37)



