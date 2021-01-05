import tkinter
from tkinter import *
import random
from tkinter import messagebox
import os
import turtle

root = Tk()

answers = [
    "BOTTLE",
    "GAMER",
    "COMPUTER",
    "SCIENCE",
    "INDIA",
    "AMERICA",
    "DUBAI",
]

jumbled_words = [
    "TOLETB",
    "MAGER",
    "PCEUORTM",
    "CEISNEC",
    "AIDIN",
    "AIEARCM",
    "BUDIA",
]

num =  random.randrange(0, len(jumbled_words), 1)

lbl = Label(
      root,
      text = "gg",
      font = ("Agency FB", 18),
      bg = "#f5756c",
      fg = "#fc1100",
  )
lbl.pack(pady = 30,ipady=10,ipadx=15)

def default():
    global jumbled_words,answers,num
    lbl.config(text = jumbled_words[num])

def res():
    global jumbled_words,answers,num
    num = random.randrange(0, len(jumbled_words), 1)
    lbl.config(text = jumbled_words[num])
    e1.delete(0, END)


def checkans():
    global jumbled_words,answers,num
    var = e1.get()
    if var == answers[num]:
        messagebox.showinfo("CORRECT", "This is probably a  correct answer")
        res()
    else:
        messagebox.showerror("WRONG", "This is probably  not Correct")
        e1.delete(0, END)

def delete2():
  screen3.destroy()

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()

def session():
  screen8 = Toplevel(screen)

  root = tkinter.Tk()
  root.geometry("450x500+175+50")
  root.title("Jumbled letters")

ans1 = StringVar()
e1 = Entry(
  root,
  font=("Agency FB", 16),
  textvariable = ans1,
)

# New segment starts here.

btncheck = Button(
  root,
  text="SUBMIT",
  font=("Agency FB", 16),
  width = 16,
  bg="#ffdbd9",
  fg="#00ff04",
  relief=GROOVE,
  command=checkans,
)
btncheck.pack(pady=20, ipadx=10, ipady=15)

btnreset = Button(
  root,
  text="RESET",
  font=("Agency FB", 16),
  width = 16,
  bg="#ffdbd9",
  fg="#fc1100",
  relief=GROOVE,
  command=res,
)
btnreset.pack(pady=20, ipadx=10, ipady=15)

default()
root.mainloop()

def login_sucess():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("Success")
  screen3.geometry("150x100")
  Label(screen3, text = "Login Sucess").pack()
  Button(screen3, text = "OK", command =delete2).pack()
  session()

def password_not_recognised():
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("Success")
  screen4.geometry("150x100")
  Label(screen4, text = "Password Error").pack()
  Button(screen4, text = "OK", command =delete3).pack()

def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("Success")
  screen5.geometry("150x100")
  Label(screen5, text = "User Not Found").pack()
  Button(screen5, text = "OK", command =delete4).pack()

  
def register_user():
  print("working")
  
  username_info = username.get()
  password_info = password.get()

  file=open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()

  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(screen1, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).pack()

def login_verify():
  
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)

  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
        login_sucess()
    else:
        password_not_recognised()

  else:
        user_not_found()
  


def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("300x250")
  
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()

  Label(screen1, text = "Please enter details below").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Username * ").pack()
 
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "Password * ").pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("300x250")
  Label(screen2, text = "Please enter details below to login").pack()
  Label(screen2, text = "").pack()

  global username_verify
  global password_verify
  
  username_verify = StringVar()
  password_verify = StringVar()

  global username_entry1
  global password_entry1
  
  Label(screen2, text = "Username * ").pack()
  username_entry1 = Entry(screen2, textvariable = username_verify)
  username_entry1.pack()
  Label(screen2, text = "").pack()
  Label(screen2, text = "Password * ").pack()
  password_entry1 = Entry(screen2, textvariable = password_verify)
  password_entry1.pack()
  Label(screen2, text = "").pack()
  Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()
  
  
def main_screen():
  global screen
  screen = Tk()
  screen.geometry("300x250")
  screen.title("Jumbled words login screen")
  Label(text = "Login/register", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  Button(text = "Login", height = "2", width = "30", command = login).pack()
  Label(text = "").pack()
  Button(text = "Register",height = "2", width = "30", command = register).pack()

  screen.mainloop()

main_screen()
