# Talha Harooni - MySQL Server
# Yasin Zahir - Python Frontend
# Jason Khalili - Python Backend
# test

import mysql.connector
import tkinter as tk
from mysql.connector import Error
from tkinter import *
from datetime import datetime


def insertItems(username):
    dropdowns = []
    reviews = []
    usernames = []

    def updateItems():
        def handleReview():
            i = 1
            t = datetime.today()
            for review in reviews:
                if (review.get()):
                    o = datetime.today().strftime("%Y-%m-%d")
                    cursor.execute(f"SELECT * FROM Reviews WHERE username='{username}' AND date='{o}'")
                    cursor.fetchall()

                    if(cursor.rowcount >= 3):
                        lblp = tk.Label(secondary_window, text = "User has already submitted three reviews today. Review not submitted.            ")
                        lblp.place(x = 400, y = 0)
                        return
                    
                    if (usernames[i-1] == username):
                        lblp = tk.Label(secondary_window, text = "Can't review your own item.                                                  ")
                        lblp.place(x = 400, y = 0)
                        return



                    r = review.get()
                    cursor.execute(f"INSERT INTO Reviews (id, username, rating, ratingText, date) VALUES (%s, %s, %s, %s, %s)", (i, username, dropdowns[i-1].get(), r, t))
                    dataBase.commit()
                    lblp = tk.Label(secondary_window, text = "Added review.                                                  ")
                    lblp.place(x = 400, y = 0)

                i += 1;    

        n = datetime.today().strftime("%Y-%m-%d")
        
        searchTerm = searchBox.get()
        title = itemTitle.get()
        description = itemDescription.get()
        category = itemCategory.get()
        price = itemPrice.get()

        if (searchTerm == ""):
            cursor.execute(f"SELECT * FROM Items WHERE username='{username}' AND date='{n}'")
            cursor.fetchall()

            if(cursor.rowcount >= 3):
                lblp = tk.Label(root, text = "User has already submitted three items today             ")
                lblp.place(x = 400, y = 170)
                return
            
            cursor.execute("INSERT INTO Items (username, title, description, category, price, date) VALUES (%s, %s, %s, %s, %s, %s)", (username, title, description, category, price, n))
            dataBase.commit()

            secondary_window = tk.Toplevel()
            secondary_window.title("List of Items")
            secondary_window.config(width=1600, height=1000)

            cursor.execute("SELECT * FROM Items")
            yIncrement = 20

            for x in cursor:
                lbl1 = tk.Label(secondary_window, text=x[1])
                lbl1.place(x = 20, y = yIncrement)

                lbl2 = tk.Label(secondary_window, text=x[2])
                lbl2.place(x = 150, y = yIncrement)

                lbl3 = tk.Label(secondary_window, text=x[3])
                lbl3.place(x = 250, y = yIncrement)

                lbl4 = tk.Label(secondary_window, text=x[4])
                lbl4.place(x = 400, y = yIncrement)

                lbl5 = tk.Label(secondary_window, text=x[5])
                lbl5.place(x = 500, y = yIncrement)

                options = [
                    "Excellent",
                    "Good",
                    "Fair",
                    "Poor"
                ]

                clicked = StringVar()
                clicked.set("Excellent")
                drop = OptionMenu(secondary_window, clicked, *options)
                drop.place(x = 550, y = yIncrement)

                reviewText = tk.Entry(secondary_window, width = 50)
                reviewText.place(x = 650, y = yIncrement, width = 100)

                reviews.append(reviewText)
                dropdowns.append(clicked)
                usernames.append(x[1])

                reviewSubmit = tk.Button(secondary_window, text ="Submit Review",
                      bg ='blue', fg= 'white', command = handleReview)
                reviewSubmit.place(x = 750, y = yIncrement, width = 100)

                yIncrement += 30
        else:
            secondary_window = tk.Toplevel()
            secondary_window.title("List of Items")
            secondary_window.config(width=1600, height=1000)

            cursor.execute(f"SELECT * FROM Items WHERE category LIKE '%{searchTerm}%'")
            yIncrement = 30

            for x in cursor:
                lbl1 = tk.Label(secondary_window, text=x[1])
                lbl1.place(x = 20, y = yIncrement)

                lbl2 = tk.Label(secondary_window, text=x[2])
                lbl2.place(x = 150, y = yIncrement)

                lbl3 = tk.Label(secondary_window, text=x[3])
                lbl3.place(x = 250, y = yIncrement)

                lbl4 = tk.Label(secondary_window, text=x[4])
                lbl4.place(x = 400, y = yIncrement)

                lbl4 = tk.Label(secondary_window, text=x[5])
                lbl4.place(x = 500, y = yIncrement)

                options = [
                    "Excellent",
                    "Good",
                    "Fair",
                    "Poor"
                ]

                clicked = StringVar()
                clicked.set("Excellent")
                drop = OptionMenu(secondary_window, clicked, *options)
                drop.place(x = 550, y = yIncrement)

                reviewText = tk.Entry(secondary_window, width = 50)
                reviewText.place(x = 650, y = yIncrement, width = 100)

                reviews.append(reviewText)
                dropdowns.append(clicked)
                usernames.append(x[1])

                reviewSubmit = tk.Button(secondary_window, text ="Submit Review",
                      bg ='blue', fg= 'white', command = handleReview)
                reviewSubmit.place(x = 750, y = yIncrement, width = 100)

                yIncrement += 30

    lbltitle = tk.Label(root, text ="Title:", )
    lbltitle.place(x = 300, y = 20)
    
    itemTitle = tk.Entry(root, width = 35)
    itemTitle.place(x = 400, y = 20, width = 100)

    lblDescription = tk.Label(root, text ="Description:", )
    lblDescription.place(x = 300, y = 50)
    
    itemDescription = tk.Entry(root, width = 35)
    itemDescription.place(x = 400, y = 50, width = 100)

    lblCategory = tk.Label(root, text ="Category:", )
    lblCategory.place(x = 300, y = 80)
    
    itemCategory = tk.Entry(root, width = 35)
    itemCategory.place(x = 400, y = 80, width = 100)

    lblPrice = tk.Label(root, text ="Price:", )
    lblPrice.place(x = 300, y = 110)
    
    itemPrice = tk.Entry(root, width = 35)
    itemPrice.place(x = 400, y = 110, width = 100)

    itemsubmit = tk.Button(root, text ="Post Item",
                      bg ='blue', fg= 'white', command = updateItems)
    itemsubmit.place(x = 400, y = 140, width = 55)

    searchLabel = tk.Label(root, text ="Search Category:", )
    searchLabel.place(x = 300, y = 200)
    
    searchBox = tk.Entry(root, width = 35)
    searchBox.place(x = 400, y = 200, width = 100)

    searchSubmit = tk.Button(root, text ="Search",
                      bg ='blue', fg= 'white', command = updateItems)
    searchSubmit.place(x = 400, y = 230, width = 55)

def register():
    user = regUsername.get()
    passw = regpassword.get()
    passwsecond = regpasswordsecond.get()
    firstname = regfirstname.get()
    lastname = reglastname.get()
    email = regemail.get()

    cursor.execute(f"SELECT * FROM User WHERE username='{user}'")
    cursor.fetchall()
    userblank = cursor.rowcount

    cursor.execute(f"SELECT * FROM User WHERE email='{email}'")
    cursor.fetchall()
    emailblank = cursor.rowcount

    if userblank != 0:
        regexistsrow = tk.Label(root, text = "Username already exists             ")
        regexistsrow.place(x = 150, y = 360)
    elif emailblank != 0:
        regexistsrow = tk.Label(root, text = "Email already exists             ")
        regexistsrow.place(x = 150, y = 360)
    elif user == "":
        regexistsrow = tk.Label(root, text = "Username field is blank                 ")
        regexistsrow.place(x = 150, y = 360)
    elif passw == "":
        regexistsrow = tk.Label(root, text = "Password field is blank                 ")
        regexistsrow.place(x = 150, y = 360)
    elif firstname == "":
        regexistsrow = tk.Label(root, text = "First Name field is blank                 ")
        regexistsrow.place(x = 150, y = 360)
    elif lastname == "":
        regexistsrow = tk.Label(root, text = "Last Name field is blank                 ")
        regexistsrow.place(x = 150, y = 360)
    elif email == "":
        regexistsrow = tk.Label(root, text = "Email field is blank                        ")
        regexistsrow.place(x = 150, y = 360)
    elif passw != passwsecond:
        regexistsrow = tk.Label(root, text = "Passwords do not match                        ")
        regexistsrow.place(x = 150, y = 360)
    else:
        regexistsrow = tk.Label(root, text = "Registration Complete                                                                              ")
        regexistsrow.place(x = 150, y = 360)
        cursor.execute("INSERT INTO User (username, password, firstname, lastname, email) VALUES (%s, %s, %s, %s, %s)", (user, passw, firstname, lastname, email))
        dataBase.commit()



def signin():
    user = Username.get()
    passw = password.get()

    cursor.execute(f"SELECT * FROM User WHERE username='{user}' AND password='{passw}'")
    cursor.fetchall()

    if cursor.rowcount == 0:
        credentialsrow = tk.Label(root, text = "Wrong info. Try again.             ")
        credentialsrow.place(x = 120, y = 110)
    else:
        credentialsrow = tk.Label(root, text = "Credentials match. Signing in!                   ")
        credentialsrow.place(x = 120, y = 110)
        insertItems(user)

def reset():
    cursor.execute("DROP TABLE IF EXISTS User")
    cursor.execute("DROP TABLE IF EXISTS Items")
    cursor.execute("DROP TABLE IF EXISTS Reviews")

    cursor.execute("CREATE TABLE IF NOT EXISTS User (username varchar(255), password varchar(255), firstName char(255), lastName char(255), email varchar(255))")
    cursor.execute("CREATE TABLE IF NOT EXISTS Items (id INT AUTO_INCREMENT PRIMARY KEY, username varchar(255), title varchar(255), description varchar(255), category varchar(255), price varchar(255), date DATE)")
    cursor.execute("CREATE TABLE Reviews (id INT, username varchar(255), rating varchar(255), ratingText varchar(255), date Date)")

    cursor.execute("INSERT INTO User (username, password, firstname, lastname, email) VALUES (%s, %s, %s, %s, %s)", ("jasonk", "password", "Jason", "Khalili", "jk@yahoo.com"))
    cursor.execute("INSERT INTO User (username, password, firstname, lastname, email) VALUES (%s, %s, %s, %s, %s)", ("johnm", "blueberry", "John", "Myers", "johnm@gmail.com"))
    cursor.execute("INSERT INTO User (username, password, firstname, lastname, email) VALUES (%s, %s, %s, %s, %s)", ("erniejohnson", "insidethenba", "Ernie", "Johnson", "erniejohnsonjr@yahoo.com"))
    cursor.execute("INSERT INTO User (username, password, firstname, lastname, email) VALUES (%s, %s, %s, %s, %s)", ("kobeb24", "basketball", "Kobe", "Bryant", "kb24@outlook.com"))
    cursor.execute("INSERT INTO User (username, password, firstname, lastname, email) VALUES (%s, %s, %s, %s, %s)", ("mahdiebrahimi", "comp440", "Mahdi", "Ebrahimi", "mahdiebrahimi@csun.edu"))

    cursor.execute("INSERT INTO Items (username, title, description, category, price, date) VALUES (%s, %s, %s, %s, %s, %s)", ("jasonk", "iPhone 15", "Brand New Iphone 15", "phone", "1,000", datetime.now()))
    cursor.execute("INSERT INTO Items (username, title, description, category, price, date) VALUES (%s, %s, %s, %s, %s, %s)", ("johnm", "iPhone 15", "Used Samsung Galaxy S23", "phone", "800", datetime.now()))
    cursor.execute("INSERT INTO Items (username, title, description, category, price, date) VALUES (%s, %s, %s, %s, %s, %s)", ("erniejohnson", "Herman Miller Aeron Chair", "Aeron chair with full lumbar support", "chair", "1,200", datetime.now()))
    cursor.execute("INSERT INTO Items (username, title, description, category, price, date) VALUES (%s, %s, %s, %s, %s, %s)", ("kobeb24", "Generic Chair", "Chair from Office Depot", "chair", "200", datetime.now()))
    cursor.execute("INSERT INTO Items (username, title, description, category, price, date) VALUES (%s, %s, %s, %s, %s, %s)", ("mahdiebrahimi", "Crystal Geyser 12oz Water", "Refreshing water", "beverage", "10", datetime.now()))

    cursor.execute("INSERT INTO Reviews (id, username, rating, ratingText, date) VALUES (%s, %s, %s, %s, %s)", (1, "jasonk", "Excellent", "This phone is too expensive.", datetime.now()))
    cursor.execute("INSERT INTO Reviews (id, username, rating, ratingText, date) VALUES (%s, %s, %s, %s, %s)", (2, "johnm", "Poor", "Good phone, wish the ui was better.", datetime.now()))
    cursor.execute("INSERT INTO Reviews (id, username, rating, ratingText, date) VALUES (%s, %s, %s, %s, %s)", (3, "erniejohnson", "Fair", "Wonderful chair. Fixed my back problems.", datetime.now()))
    cursor.execute("INSERT INTO Reviews (id, username, rating, ratingText, date) VALUES (%s, %s, %s, %s, %s)", (4, "kobeb24", "Good", "This chair made me lose my ability to walk", datetime.now()))
    cursor.execute("INSERT INTO Reviews (id, username, rating, ratingText, date) VALUES (%s, %s, %s, %s, %s)", (5, "mahdiebrahimi", "Fair", "Refreshing!!!", datetime.now()))


    dataBase.commit()

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
cursor.execute("SELECT * FROM User")

for x in cursor:
    print(x)

root = tk.Tk()
root.geometry("900x600")
root.title("DBMS Login Page")
  
 
# Defining the first row
lblfrstrow = tk.Label(root, text ="Username:", )
lblfrstrow.place(x = 50, y = 20)
 
Username = tk.Entry(root, width = 35)
Username.place(x = 150, y = 20, width = 100)
  
lblsecrow = tk.Label(root, text ="Password:")
lblsecrow.place(x = 50, y = 50)
 
password = tk.Entry(root, width = 35)
password.place(x = 150, y = 50, width = 100)

submitbtn = tk.Button(root, text ="Login",
                      bg ='blue', fg= 'white', command = signin)
submitbtn.place(x = 150, y = 80, width = 55)


regfirstrow = tk.Label(root, text = "Username: ")
regfirstrow.place(x = 50, y = 150)

regUsername = tk.Entry(root, width = 35)
regUsername.place(x = 150, y = 150, width = 100)

regsecondrow = tk.Label(root, text = "Password: ")
regsecondrow.place(x = 50, y = 180)

regpassword = tk.Entry(root, width = 35)
regpassword.place(x = 150, y = 180, width = 100)

regsecondrow = tk.Label(root, text = "Password: ")
regsecondrow.place(x = 50, y = 210)

regpasswordsecond = tk.Entry(root, width = 35)
regpasswordsecond.place(x = 150, y = 210, width = 100)

regthirdrow = tk.Label(root, text = "First Name: ")
regthirdrow.place(x = 50, y = 240)

regfirstname = tk.Entry(root, width = 35)
regfirstname.place(x = 150, y = 240, width = 100)

regfourthrow = tk.Label(root, text = "Last Name: ")
regfourthrow.place(x = 50, y = 270)

reglastname = tk.Entry(root, width = 35)
reglastname.place(x = 150, y = 270, width = 100)

regfifthrow = tk.Label(root, text = "Email: ")
regfifthrow.place(x = 50, y = 300)

regemail = tk.Entry(root, width = 35)
regemail.place(x = 150, y = 300, width = 100)

registerbtn = tk.Button(root, text = "Register",
                        bg = 'blue', fg='white', command = register)
registerbtn.place(x = 150, y = 330, width = 55)

resetbutton = tk.Button(root, text = "Initialize Database",
                        bg = 'blue', fg='white', command = reset)
resetbutton.place(x = 100, y = 390, width = 155)

 
root.mainloop()

dataBase.close()