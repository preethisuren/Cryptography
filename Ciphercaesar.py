import tkinter as tk
from tkinter import *
import tkinter.font as tkfont
from tkinterhtml import HtmlFrame


root = tk.Tk()                   #create the window

root.title("Caesar Cipher")      # For title bar 
root.geometry("490x360")         #set the dimensions (width x height)

canvas = tk.Canvas(root,height = 360, width=490, bg="#7FFF00")  # Creating a canvas 
canvas.pack()                                                   # Attaching the created canvas


txtfont = tkfont.Font(family="Courier New",size=12,weight="bold")  #fonts

#message
label1 = tk.Label(root,text= "Enter the message: ",width=19,bg="#7FFF00")
# adding the font features to the label
label1.config(font=txtfont)
# placing the label in the canvas
canvas.create_window(100,20,window=label1)

# Text Area to get input (message)
label1_text = tk.Entry(root)
canvas.create_window(250,20,window=label1_text)

#key
label2 = tk.Label(root,text="Enter Key b/w 0-26: ", width=20,bg="#7FFF00")
label2.config(font=txtfont)
# placing the label in the canvas
canvas.create_window(100,50,window=label2)

# Text Area to get input (key)
label2_text = tk.Entry(root)
canvas.create_window(250,50,window=label2_text)

#Tkinter Variable 
v = tk.IntVar()

def choice():
  # Get the value of the radio button
    x = v.get()
  # Performs Encryption if the value is 1 else performs Decryption.
    if(x==1):
        encryption()
    elif(x==2):
        decryption()


# for encryption
def encryption():
	# Get the user entered text to get function and store it in a variable plain_text
	plain_text = label1_text.get()
	# To store the result   
	cipher_text = ""
    # Get the user entered key to do shift and store it in a variable key
	key = int(label2_text.get())

	for i in range(len(plain_text)): #length of entered message
	    letter = plain_text[i]
	# UpperCase 
	    if(letter.isupper()):
	        cipher_text+=chr((ord(letter)+key-65)%26+65)
	    else:
	# LowerCase
	        cipher_text+=chr((ord(letter)+key-97)%26+97)

	# Creating a label with a text and attaching it to the root       
	label3 =tk.Label(root,text=cipher_text,width=100,bg="white")

	# adding the font features to the label
	label3.config (font=txtfont)
	label3_text = tk.Entry(root)
	canvas.create_window(300,160,window=label3)

	

# for Decryption
def decryption():
	# Get the user entered text to get function and store it in a varaible cipher_text
	cipher_text = label1_text.get()
	# To store the result
	plain_text = ""
	# Number of shifts to be performed
	key = int(label2_text.get())

	for i in range(len(cipher_text)):
	    letter = cipher_text[i]
	# Uppercase
	    if(letter.isupper()):
	        plain_text+=chr((ord(letter)-key-65)%26+65)
	    else:
	# Lowercase
	        plain_text+=chr((ord(letter)-key-97)%26+97) 
	        # Creating a label with a text and attaching it to the root
	    label4 =tk.Label(root,text=plain_text,width=30,bg="white")

	  # Adding the font features to the label
	    label4.config(font=txtfont)
	    canvas.create_window(300,160,window=label4)

# Radio Button for Encryption 
label5=tk.Radiobutton(root, text="Encryption",padx = 20, variable=v, value=1,command=choice,bg="#7FFF00")
label5.config(font=txtfont)
canvas.create_window(100,100,window=label5)
# Radio Button for Decryption
label6=tk.Radiobutton(root, text="Decryption",padx = 20, variable=v, value=2,command=choice,bg="#7FFF00")
label6.config(font=txtfont)
canvas.create_window(300,100,window=label6)


# Creating a label with a text and attaching it to the root
label7 =tk.Label(root,text="Converted Text 	: ",width=20,bg="#7FFF00")
# adding the font features to the label
label7.config(font=txtfont)
# placing the label in the canvas
canvas.create_window(100,160,window=label7)





root.mainloop()


