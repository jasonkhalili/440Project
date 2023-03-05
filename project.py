import mysql.connector
import tkinter as tk
from mysql.connector import Error
from tkinter import *

def register():
    user = regUsername.get()
    passw = regpassword.get()
    firstname = regfirstname.get()
    lastname = reglastname.get()
    email = regemail.get()

    cursor.execute(f"SELECT * FROM User WHERE username='{user}'")
    cursor.fetchall()

    if cursor.rowcount != 0:
        regexistsrow = tk.Label(root, text = "Username already exists             ")
        regexistsrow.place(x = 150, y = 330)
    elif user == "":
        regexistsrow = tk.Label(root, text = "Username field is blank                 ")
        regexistsrow.place(x = 150, y = 330)
    elif passw == "":
        regexistsrow = tk.Label(root, text = "Password field is blank                 ")
        regexistsrow.place(x = 150, y = 330)
    elif firstname == "":
        regexistsrow = tk.Label(root, text = "First Name field is blank                 ")
        regexistsrow.place(x = 150, y = 330)
    elif lastname == "":
        regexistsrow = tk.Label(root, text = "Last Name field is blank                 ")
        regexistsrow.place(x = 150, y = 330)
    elif email == "":
        regexistsrow = tk.Label(root, text = "Email field is blank                        ")
        regexistsrow.place(x = 150, y = 330)
    else:
        regexistsrow = tk.Label(root, text = "                                                                                  ")
        regexistsrow.place(x = 150, y = 330)

    cursor.execute("INSERT INTO User (username, password, firstname, lastname, email) VALUES (%s, %s, %s, %s, %s)", (user, passw, firstname, lastname, email))


def submission():
     user = Username.get()
     passw = password.get()

     print(user)
     print(passw)

try:
    dataBase = mysql.connector.connect(
                        host = "localhost",
                        user = "root",
                        passwd = "password",
                        database = "students" 
                    )
    print("Connection successful")
except Error as e:
    print(f"The error '{e}' occurred")

cursor = dataBase.cursor()

# cursor.execute("CREATE TABLE User (username varchar(255), password varchar(255), firstName char(255), lastName char(255), email varchar(255))")
# cursor.execute("INSERT INTO User (username, password, firstname, lastname, email) VALUES (%s, %s, %s, %s, %s)", ("jasonk", "password", "jason", "khalili", "jk@yahoo.com"))
cursor.execute("SELECT * FROM User")

for x in cursor:
    print(x)

root = tk.Tk()
root.geometry("300x600")
root.title("DBMS Login Page")
  
 
# Defining the first row
lblfrstrow = tk.Label(root, text ="Username -", )
lblfrstrow.place(x = 50, y = 20)
 
Username = tk.Entry(root, width = 35)
Username.place(x = 150, y = 20, width = 100)
  
lblsecrow = tk.Label(root, text ="Password -")
lblsecrow.place(x = 50, y = 50)
 
password = tk.Entry(root, width = 35)
password.place(x = 150, y = 50, width = 100)

submitbtn = tk.Button(root, text ="Login",
                      bg ='blue', command = submission)
submitbtn.place(x = 150, y = 80, width = 55)


regfirstrow = tk.Label(root, text = "Username: ")
regfirstrow.place(x = 50, y = 150)

regUsername = tk.Entry(root, width = 35)
regUsername.place(x = 150, y = 150, width = 100)

regsecondrow = tk.Label(root, text = "Password: ")
regsecondrow.place(x = 50, y = 180)

regpassword = tk.Entry(root, width = 35)
regpassword.place(x = 150, y = 180, width = 100)

regthirdrow = tk.Label(root, text = "First Name: ")
regthirdrow.place(x = 50, y = 210)

regfirstname = tk.Entry(root, width = 35)
regfirstname.place(x = 150, y = 210, width = 100)

regfourthrow = tk.Label(root, text = "Last Name: ")
regfourthrow.place(x = 50, y = 240)

reglastname = tk.Entry(root, width = 35)
reglastname.place(x = 150, y = 240, width = 100)

regfifthrow = tk.Label(root, text = "Email: ")
regfifthrow.place(x = 50, y = 270)

regemail = tk.Entry(root, width = 35)
regemail.place(x = 150, y = 270, width = 100)

registerbtn = tk.Button(root, text = "Register",
                        bg = 'blue', command = register)
registerbtn.place(x = 150, y = 300, width = 55)

 
root.mainloop()

dataBase.close()