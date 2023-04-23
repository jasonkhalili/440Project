# Talha Harooni - MySQL Server
# Yasin Zahir - Python Frontend
# Jason Khalili - Python Backend

import time
import mysql.connector
import tkinter as tk
from mysql.connector import Error
from tkinter import *
from datetime import datetime


def insertItems(username):
    dropdowns = []
    reviews = []
    usernames = []

    def mostExpensivePerCategory():
        third_window = tk.Toplevel()
        third_window.title("List of Items")
        third_window.config(width=1600, height=1000)

        cursor.execute(f"SELECT * FROM Items WHERE (category, price) IN (SELECT category, MAX(price) FROM Items GROUP BY category)")
        
        yIncrement = 30

        for x in cursor:
            lbl1 = tk.Label(third_window, text=x[1])
            lbl1.place(x = 20, y = yIncrement)

            lbl2 = tk.Label(third_window, text=x[2])
            lbl2.place(x = 150, y = yIncrement)

            lbl3 = tk.Label(third_window, text=x[3])
            lbl3.place(x = 300, y = yIncrement)

            lbl4 = tk.Label(third_window, text=x[4])
            lbl4.place(x = 600, y = yIncrement)

            lbl5 = tk.Label(third_window, text=x[5])
            lbl5.place(x = 700, y = yIncrement)

            yIncrement += 30

    def twoItemsSameDay(uno, dos):
        third_window = tk.Toplevel()
        third_window.title("List of Items")
        third_window.config(width=800, height=1000)

        cursor.execute(f"SELECT DISTINCT u.username FROM User u JOIN Items i1 ON u.username = i1.username JOIN Items i2 ON u.username = i2.username AND i1.id <> i2.id WHERE i1.category = '{uno}' AND i2.category = '{dos}' AND i1.date = i2.date")
        
        yIncrement = 30

        for x in cursor:
            lbl1 = tk.Label(third_window, text=x[0])
            lbl1.place(x = 20, y = yIncrement)

            yIncrement += 30

    def excellentOrGood(u):
        third_window = tk.Toplevel()
        third_window.title("List of Items")
        third_window.config(width=800, height=1000)

        cursor.execute(f"SELECT i.id, i.title, r.rating FROM Items i JOIN Reviews r ON i.id = r.id WHERE i.username = '{u}' AND r.rating IN ('Excellent', 'Good') AND i.id NOT IN ( SELECT r2.id FROM Reviews r2 WHERE r2.rating NOT IN ('Excellent', 'Good'))")

        yIncrement = 30

        for x in cursor:
            lbl1 = tk.Label(third_window, text=x[1])
            lbl1.place(x = 20, y = yIncrement)

            yIncrement += 30

    def usersMostItems():
        third_window = tk.Toplevel()
        third_window.title("List of Items")
        third_window.config(width=800, height=1000)

        cursor.execute(f"SELECT u.username, COUNT(*) as num_items FROM User u JOIN Items i ON u.username = i.username WHERE i.date >= '2020-05-01' GROUP BY u.username HAVING COUNT(*) = (SELECT COUNT(*) FROM Items i2 WHERE i2.date >= '2020-05-01' GROUP BY i2.username ORDER BY COUNT(*) DESC LIMIT 1)")

        yIncrement = 30

        for x in cursor:
            lbl1 = tk.Label(third_window, text=x[0])
            lbl1.place(x = 20, y = yIncrement)

            yIncrement += 30

    def neverExcellent():
        third_window = tk.Toplevel()
        third_window.title("List of Items")
        third_window.config(width=800, height=1000)

        cursor.execute(f"SELECT DISTINCT u.username FROM User u LEFT JOIN Items i ON i.username = u.username LEFT JOIN (SELECT id, COUNT(*) AS excellent_reviews FROM Reviews WHERE rating = 'excellent' GROUP BY id HAVING COUNT(*) >= 3) e ON e.id = i.id LEFT JOIN Reviews r ON r.id = i.id AND r.rating <> 'excellent' WHERE e.id IS NULL AND r.rating IS NULL;")

        yIncrement = 30

        for x in cursor:
            lbl1 = tk.Label(third_window, text=x[0])
            lbl1.place(x = 20, y = yIncrement)

            yIncrement += 30

    def neverPoor():
        third_window = tk.Toplevel()
        third_window.title("List of Items")
        third_window.config(width=800, height=1000)

        cursor.execute(f"SELECT DISTINCT u.username FROM User u LEFT JOIN Reviews r ON u.username = r.username WHERE r.rating <> 'Poor' OR r.rating IS NULL")

        yIncrement = 30

        for x in cursor:
            lbl1 = tk.Label(third_window, text=x[0])
            lbl1.place(x = 20, y = yIncrement)

            yIncrement += 30

    def eachPoor():
        third_window = tk.Toplevel()
        third_window.title("List of Items")
        third_window.config(width=800, height=1000)

        cursor.execute(f"SELECT DISTINCT u.username FROM User u INNER JOIN Reviews r ON u.username = r.username LEFT JOIN (SELECT DISTINCT username FROM Reviews WHERE rating <> 'poor' OR rating IS NULL) p ON u.username = p.username WHERE p.username IS NULL;")

        yIncrement = 30

        for x in cursor:
            lbl1 = tk.Label(third_window, text=x[0])
            lbl1.place(x = 20, y = yIncrement)

            yIncrement += 30

    def noPoorReviews():
        third_window = tk.Toplevel()
        third_window.title("List of Items")
        third_window.config(width=800, height=1000)

        cursor.execute(f"SELECT DISTINCT u.username FROM User u INNER JOIN Items i ON u.username = i.username LEFT JOIN (SELECT DISTINCT id FROM Reviews WHERE rating = 'poor') p ON i.id = p.id LEFT JOIN (SELECT DISTINCT id, COUNT(*) AS review_count FROM Reviews GROUP BY id ) c ON i.id = c.id WHERE p.id IS NULL AND (c.review_count IS NULL OR c.review_count = 0)")

        yIncrement = 30

        for x in cursor:
            lbl1 = tk.Label(third_window, text=x[0])
            lbl1.place(x = 20, y = yIncrement)

            yIncrement += 30

    def eachOtherExcellent():
        third_window = tk.Toplevel()
        third_window.title("List of Items")
        third_window.config(width=800, height=1000)

        cursor.execute(f"SELECT DISTINCT i1.username AS userA, i2.username AS userB FROM Items i1 INNER JOIN Items i2 INNER JOIN Reviews r1 ON i1.id = r1.id AND i2.username = r1.username AND r1.rating = 'excellent'INNER JOIN Reviews r2 ON i2.id = r2.id AND i1.username = r2.username AND r2.rating = 'excellent';")

        yIncrement = 30

        for x in cursor:
            placeholder = f"({x[0]}, {x[1]})"
            lbl1 = tk.Label(third_window, text=placeholder)
            lbl1.place(x = 20, y = yIncrement)

            yIncrement += 30


    def updateItems():
        dropdowns.clear()
        reviews.clear()
        usernames.clear()
        
        itemid = 0
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
                    cursor.execute(f"INSERT INTO Reviews (id, username, rating, ratingText, date) VALUES (%s, %s, %s, %s, %s)", (itemid, username, dropdowns[i-1].get(), r, t))
                    dataBase.commit()
                    lblp = tk.Label(secondary_window, text = "Added review.                                                                                                                    ")
                    lblp.place(x = 400, y = 0)

                i += 1;


        n = datetime.today().strftime("%Y-%m-%d")
        
        searchTerm = searchBox.get()
        title = itemTitle.get()
        description = itemDescription.get()
        category = itemCategory.get()
        price = itemPrice.get()
        price = int(price)

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
            yIncrement = 30

            for x in cursor:
                lbl1 = tk.Label(secondary_window, text=x[1])
                lbl1.place(x = 20, y = yIncrement)

                lbl2 = tk.Label(secondary_window, text=x[2])
                lbl2.place(x = 150, y = yIncrement)

                lbl3 = tk.Label(secondary_window, text=x[3])
                lbl3.place(x = 300, y = yIncrement)

                lbl4 = tk.Label(secondary_window, text=x[4])
                lbl4.place(x = 600, y = yIncrement)

                lbl5 = tk.Label(secondary_window, text=x[5])
                lbl5.place(x = 700, y = yIncrement)

                options = [
                    "Excellent",
                    "Good",
                    "Fair",
                    "Poor"
                ]

                clicked = StringVar()
                clicked.set("Excellent")
                drop = OptionMenu(secondary_window, clicked, *options)
                drop.place(x = 750, y = yIncrement)

                reviewText = tk.Entry(secondary_window, width = 50)
                reviewText.place(x = 850, y = yIncrement, width = 100)

                itemid = x[0]

                reviews.append(reviewText)
                dropdowns.append(clicked)
                usernames.append(x[1])

                reviewSubmit = tk.Button(secondary_window, text ="Submit Review",
                      bg ='blue', fg= 'white', command = handleReview)
                reviewSubmit.place(x = 950, y = yIncrement, width = 100)

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
                lbl3.place(x = 300, y = yIncrement)

                lbl4 = tk.Label(secondary_window, text=x[4])
                lbl4.place(x = 600, y = yIncrement)

                lbl4 = tk.Label(secondary_window, text=x[5])
                lbl4.place(x = 700, y = yIncrement)

                options = [
                    "Excellent",
                    "Good",
                    "Fair",
                    "Poor"
                ]

                clicked = StringVar()
                clicked.set("Excellent")
                drop = OptionMenu(secondary_window, clicked, *options)
                drop.place(x = 750, y = yIncrement)

                reviewText = tk.Entry(secondary_window, width = 50)
                reviewText.place(x = 850, y = yIncrement, width = 100)

                itemid = x[0]

                reviews.append(reviewText)
                dropdowns.append(clicked)
                usernames.append(x[1])

                reviewSubmit = tk.Button(secondary_window, text ="Submit Review",
                      bg ='blue', fg= 'white', command = handleReview)
                reviewSubmit.place(x = 950, y = yIncrement, width = 100)

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



    one = tk.Button(root, text ="Most Expensive By Category",
                      bg ='blue', fg= 'white', command = mostExpensivePerCategory)
    one.place(x = 600, y = 20, width = 400)


    twoEntryOne = tk.Entry(root, width = 35)
    twoEntryOne.place(x = 600, y = 60, width = 100)

    twoEntryTwo = tk.Entry(root, width = 35)
    twoEntryTwo.place(x = 710, y = 60, width = 100)

    two = tk.Button(root, text ="Users with posts on same day, different categories",
                      bg ='blue', fg= 'white', command = lambda: twoItemsSameDay(twoEntryOne.get(), twoEntryTwo.get()))
    two.place(x = 600, y = 90, width = 400)


    threeEntry = tk.Entry(root, width = 35)
    threeEntry.place(x = 600, y = 130, width = 100)

    three = tk.Button(root, text ="Items posted by user, only 'Excellent' or 'Good' reviews",
                      bg ='blue', fg= 'white', command = lambda: excellentOrGood(threeEntry.get()))
    three.place(x = 600, y = 160, width = 400)


    four = tk.Button(root, text ="Users who posted the most items",
                      bg ='blue', fg= 'white', command = usersMostItems)
    four.place(x = 600, y = 200, width = 400)


    six = tk.Button(root, text ="Users who never posted an excellent item",
                      bg ='blue', fg= 'white', command = neverExcellent)
    six.place(x = 600, y = 230, width = 400)


    seven = tk.Button(root, text ="Users who never posted a poor review",
                      bg ='blue', fg= 'white', command = neverPoor)
    seven.place(x = 600, y = 260, width = 400)


    eight = tk.Button(root, text ="Users posted reviews, but each is 'poor'",
                      bg ='blue', fg= 'white', command = eachPoor)
    eight.place(x = 600, y = 290, width = 400)


    nine = tk.Button(root, text ="Users such that each item they posted hasn't received any 'poor' reviews",
                      bg ='blue', fg= 'white', command = noPoorReviews)
    nine.place(x = 600, y = 320, width = 400)


    ten = tk.Button(root, text ="User pairs that alwasy gave each other 'excellent' reviews",
                      bg ='blue', fg= 'white', command = eachOtherExcellent)
    ten.place(x = 600, y = 350, width = 400)

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
    cursor.execute("CREATE TABLE IF NOT EXISTS Items (id INT AUTO_INCREMENT PRIMARY KEY, username varchar(255), title varchar(255), description varchar(255), category varchar(255), price int, date DATE)")
    cursor.execute("CREATE TABLE Reviews (id INT, username varchar(255), rating varchar(255), ratingText varchar(255), date Date)")

    cursor.execute("INSERT INTO User (username, password, firstname, lastname, email) VALUES (%s, %s, %s, %s, %s)", ("jasonk", "password", "Jason", "Khalili", "jk@yahoo.com"))
    cursor.execute("INSERT INTO User (username, password, firstname, lastname, email) VALUES (%s, %s, %s, %s, %s)", ("johnm", "blueberry", "John", "Myers", "johnm@gmail.com"))
    cursor.execute("INSERT INTO User (username, password, firstname, lastname, email) VALUES (%s, %s, %s, %s, %s)", ("erniejohnson", "insidethenba", "Ernie", "Johnson", "erniejohnsonjr@yahoo.com"))
    cursor.execute("INSERT INTO User (username, password, firstname, lastname, email) VALUES (%s, %s, %s, %s, %s)", ("kobeb24", "basketball", "Kobe", "Bryant", "kb24@outlook.com"))
    cursor.execute("INSERT INTO User (username, password, firstname, lastname, email) VALUES (%s, %s, %s, %s, %s)", ("mahdiebrahimi", "comp440", "Mahdi", "Ebrahimi", "mahdiebrahimi@csun.edu"))

    cursor.execute("INSERT INTO Items (username, title, description, category, price, date) VALUES (%s, %s, %s, %s, %s, %s)", ("johnm", "iPhone 15", "Brand New Iphone 15", "phone", 1000, datetime.now()))
    cursor.execute("INSERT INTO Items (username, title, description, category, price, date) VALUES (%s, %s, %s, %s, %s, %s)", ("johnm", "Samsung Galaxy S23", "Used Samsung Galaxy S23", "phone", 800, datetime.now()))
    cursor.execute("INSERT INTO Items (username, title, description, category, price, date) VALUES (%s, %s, %s, %s, %s, %s)", ("johnm", "BWM 328i", "Brand New BMW 328i", "car", 50000, datetime.now()))
    cursor.execute("INSERT INTO Items (username, title, description, category, price, date) VALUES (%s, %s, %s, %s, %s, %s)", ("johnm", "Toyota Corolla", "Used Toyota Corolla", "car", 20000, datetime.now()))
    cursor.execute("INSERT INTO Items (username, title, description, category, price, date) VALUES (%s, %s, %s, %s, %s, %s)", ("erniejohnson", "Herman Miller Aeron Chair", "Aeron chair with full lumbar support", "chair", 1200, datetime.now()))
    cursor.execute("INSERT INTO Items (username, title, description, category, price, date) VALUES (%s, %s, %s, %s, %s, %s)", ("kobeb24", "Generic Chair", "Chair from Office Depot", "chair", 200, datetime.now()))
    cursor.execute("INSERT INTO Items (username, title, description, category, price, date) VALUES (%s, %s, %s, %s, %s, %s)", ("mahdiebrahimi", "Crystal Geyser 12oz Water", "Refreshing water", "beverage", 10, datetime.now()))
    cursor.execute("INSERT INTO Items (username, title, description, category, price, date) VALUES (%s, %s, %s, %s, %s, %s)", ("jasonk", "Nvidia 4090 Graphics Card", "High End Graphics Card", "GPU", 1000, datetime.now()))
    cursor.execute("INSERT INTO Items (username, title, description, category, price, date) VALUES (%s, %s, %s, %s, %s, %s)", ("jasonk", "AMD Radeon HD 7850", "Old Graphics Card", "GPU", 300, datetime.now()))


    cursor.execute("INSERT INTO Reviews (id, username, rating, ratingText, date) VALUES (%s, %s, %s, %s, %s)", (1, "jasonk", "Excellent", "This phone is too expensive.", datetime.now()))
    cursor.execute("INSERT INTO Reviews (id, username, rating, ratingText, date) VALUES (%s, %s, %s, %s, %s)", (2, "johnm", "Good", "Good phone, wish the ui was better.", datetime.now()))
    cursor.execute("INSERT INTO Reviews (id, username, rating, ratingText, date) VALUES (%s, %s, %s, %s, %s)", (3, "erniejohnson", "Good", "Wonderful chair. Fixed my back problems.", datetime.now()))
    cursor.execute("INSERT INTO Reviews (id, username, rating, ratingText, date) VALUES (%s, %s, %s, %s, %s)", (4, "kobeb24", "Poor", "This chair made me lose my ability to walk", datetime.now()))
    cursor.execute("INSERT INTO Reviews (id, username, rating, ratingText, date) VALUES (%s, %s, %s, %s, %s)", (5, "mahdiebrahimi", "Excellent", "Refreshing!!!", datetime.now()))
    cursor.execute("INSERT INTO Reviews (id, username, rating, ratingText, date) VALUES (%s, %s, %s, %s, %s)", (1, "jasonk", "Excellent", "Perfect!", datetime.now()))
    cursor.execute("INSERT INTO Reviews (id, username, rating, ratingText, date) VALUES (%s, %s, %s, %s, %s)", (1, "jasonk", "Excellent", "Amazing!", datetime.now()))
    cursor.execute("INSERT INTO Reviews (id, username, rating, ratingText, date) VALUES (%s, %s, %s, %s, %s)", (7, "erniejohnson", "Excellent", "Amazing!", datetime.now()))
    



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
root.geometry("1200x600")
root.title("DBMS Login Page")
  

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