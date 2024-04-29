from tkinter import *
import string
import random


def generator():
    small_alphabet = string.ascii_lowercase
    capital_alphabet = string.ascii_uppercase
    number = string.digits
    special_character = string.punctuation
    all= small_alphabet+capital_alphabet+number+special_character
    password_length = int(length_of_box.get())
    if choice.get() == 1:
        passwordfield.insert(0,random.sample( small_alphabet,password_length))
    if choice.get() == 2:
        passwordfield.insert(0,random.sample( small_alphabet+capital_alphabet,password_length))
    if choice.get() == 3:
        passwordfield.insert(0,random.sample(all,password_length))






root = Tk()
root.config(bg="orange")
choice = IntVar()
font = ("aerial",13,'bold')

password_label = Label(root,text = "PASSWORD GENERATOR",font=('Georgia',20,'bold'),bg="orange",fg='gray20')
password_label.grid()

weakradiobutton  = Radiobutton(root,text='weak',value=1,variable=choice,font= font)
weakradiobutton.grid(pady=5)

mediumradiobutton  = Radiobutton(root,text='medium',value=2,variable=choice,font= font)
mediumradiobutton.grid(pady=5)

strongradiobutton  = Radiobutton(root,text='strong',value=3,variable=choice,font= font)
strongradiobutton.grid(pady=5)

password_label = Label(root,text = "Select the length of password",font=('candara'),bg="orange",fg='gray20')
password_label.grid()

length_of_box = Spinbox(root,from_=5,to=18,width=5,font=font)
length_of_box.grid(pady=5)

generatebutton = Button(root,text="Generate Password",font=font,command=generator)
generatebutton.grid(pady=6)

passwordfield = Entry(root,width=25,bd=3,font=font)                  
passwordfield.grid(pady=5)

copybutton = Button(root,text="Copy",font=font)
copybutton.grid(pady=5)



root.mainloop()