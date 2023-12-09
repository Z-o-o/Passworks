import os
import time
import threading
import sys
from tkinter import *
from tkinter import Button, Tk
from tkinter import messagebox
from PasswordChecker import Checker
from PasswordGenerator import generator

result_text = ''
    
def analyze_password(password):
  check = Checker(password).check()
  if check != "Valid password":
    messagebox.showerror('Error', check)
  else:
    messagebox.showinfo("Info", check + ": " +str(Checker(password).analyze_password()))
  return

def generate_password():
  result_text.set(str(generator(100, 100)))
  copy_to_clipboard = Button(root, text="Copy To Clipboard", command=copy_password)
  copy_to_clipboard.pack()
  return

def copy_password():
  root.clipboard_clear()
  root.clipboard_append(result_text.get())
  root.update()
  status.config(text = "Copied to Clipboard!")
  messagebox.showinfo('Info', "Copied to Clipboard!")
  return

root = Tk()
root.title("Passworks")
root.geometry("600x320")
result_text = StringVar(master=root, value='')

row = Frame(root)
lab = Label(row, width=20, text="Type Password:", anchor='w')
ent = Entry(row)
row.pack(side=TOP, fill=X, padx=5, pady=5)
lab.pack(side=LEFT)
ent.pack(side=RIGHT, expand=YES, fill=X)


status = Label(root, text="Passworks", relief=SUNKEN, anchor=W, bd=2)

buttonRow = Frame(root)
runButton = Button(buttonRow, text='Analyze Password', command=(lambda e=ent: analyze_password(e.get())))
generateButton = Button(buttonRow, text='Generate Password', command=generate_password)
buttonRow.pack(side=TOP, fill=X, padx=5, pady=5)
runButton.pack(side=LEFT)
generateButton.pack(side=RIGHT)

result = Entry(root, width=50, text=result_text, state=DISABLED)
result.pack()

status.pack(side=BOTTOM, fill=X)

root.mainloop()