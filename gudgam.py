from tkinter import *
import os
import random
from tkinter import messagebox
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


root.geometry("450x500+175+50")
root.title("Jumbled letters")
root.configure(background = "#f5756c")

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


ans1 = StringVar()
e1 = Entry(
  root,
  font=("Agency FB", 16),
  textvariable = ans1,
)
e1.pack(pady= 20,ipady=5,ipadx=5)


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



def delete2():
  screen3.destroy()

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()
  
def login_sucess():
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

def logout():
    screen7.destroy()

def saved():
    screen10 = Toplevel(screen)
    screen10.title("saved")
    screen10.geometry("500x500")
    Label(screen10,text="Your Score Has Been Saved!").pack()


def save():
    name= raw_name.get()
    enterscore= raw_enterscore.get()
    data= open(name,"w")
    data.write(enterscore)
    data.close()
    saved()

def enterscore():
    global raw_name
    raw_name = StringVar()
    global raw_enterscore
    raw_enterscore = StringVar()
    screen9 = Toplevel(screen)
    screen9.title("Enter Score")
    screen9.geometry("500x500")
    Label(screen9,text="Please Enter Your Name here:").pack()
    Entry(screen9, textvariable= raw_name).pack()
    Label(screen9,text="Please Enter Your Score here:").pack()
    Entry(screen9, textvariable= raw_enterscore).pack()
    Button(screen9,text="save",command= save).pack()

def deletescore1():
  name3= raw_name2.get()
  os.remove(name3)
  screen14 = Toplevel(screen)
  screen14.title("LeaderBoard")
  screen14.geometry("500x500")
  Label(screen14,text= name3+" removed").pack()


def deletescore():
  screen13 = Toplevel(screen)
  screen13.title("LeaderBoard")
  screen13.geometry("500x500")
  allscores= os.listdir()
  Label(screen13,text= "these are all the scores").pack()
  Label(screen13,text= allscores).pack()
  global raw_name2
  raw_name2= StringVar()
  Entry(screen13, textvariable= raw_name2).pack()
  Button(screen13,command= deletescore1,text= "ok").pack()



def viewscore1():
  name1= raw_name1.get()
  data = open(name1,"r")
  data1= data.read()
  screen12 = Toplevel(screen)
  screen12.title("LeaderBoard")
  screen12.geometry("500x500")
  Label(screen12,text= data1).pack()
  
def viewscore():
    screen11 = Toplevel(screen)
    screen11.title("LeaderBoard")
    screen11.geometry("500x500")
    allscores= os.listdir()
    Label(screen11,text= "these are all the scores").pack()
    Label(screen11,text= allscores).pack()
    global raw_name1
    raw_name1= StringVar()
    Entry(screen11, textvariable= raw_name1).pack()
    Button(screen11,command= viewscore1,text= "ok").pack()


def session():
    screen8 = Toplevel(screen)
    screen8.title("GREAT!")
    screen8.geometry("500x500")
    Label(screen8,text="You Win! ").pack()
    Button(screen8,text= "Enter score ", command = enterscore).pack()
    Button(screen8,text= "View Score ",command= viewscore).pack()
    Button(screen8,text= "Delete Entry ",command= deletescore).pack()



  
def main_screen():
  global screen
  screen = Tk()
  screen.geometry("300x250")
  screen.title("Jumbled Letters")
  Label(text = "Jumbled Letters", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  Button(text = "Login", height = "2", width = "30", command = login).pack()
  Label(text = "").pack()
  Button(text = "Register",height = "2", width = "30", command = register).pack()

  screen.mainloop()

main_screen()
  
