from tkinter import *
from tkinter import StringVar
import re

# writing information on output file starts
def write_data():
    # checks email pattern
    email_sp_info = email_sp.get()
    pattern = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
    if (re.search( pattern, email_sp_info )):
        Label(screen_sp,
              text="Valid Email",
              fg="green",
              font=("calibri", 11)).place(x=15, y=120)

        password_sp_info = password_sp.get()
        confirm_password_sp_info = confirm_sp_password.get()

        # checks password and confirm password is same or not
        if (password_sp_info == confirm_password_sp_info):
            Label(screen_sp,
                  text="Registration Successful",
                  fg="green",
                  font=("calibri", 11)).place(x=15, y=350)

        # writes Sing Up data in database_output file
            file_sp = open("database_output.txt", "a")
            file_sp.write(email_sp_info + " " + password_sp_info)
            file_sp.write("\n")
            file_sp.close()
        else:
            Label(screen_sp,
                  text="Password does not match",
                  fg="red",
                  font=("calibri", 11)).place(x=15, y=350)

    else:
        Label(screen_sp,
              text="Invalid Email",
              fg="red",
              font=("calibri", 11)).place(x=15, y=120)

    # clears input entry after function is called
    email_sp_text_entry.delete(0, END)
    password_sp_text_entry.delete(0, END)
    confirm_sp_password_text_entry.delete(0, END)
    screen_sp.mainloop()
# writing information on output file end


# checking information from input screen starts
def check_info_input():
    # takes input from Sign In GUI window
    email_info = email.get()
    pass_info = password.get()
    # clears input entry after function is called
    email_text_entry.delete(0, END)
    password_text_entry.delete(0, END)
    file = open("database.txt", "r")
    lst = file.readlines()
    file.close()
    match = False
    inc = 0

    # removes \n from each line in the database
    for elmnt in lst:
        elmnt = elmnt.strip('\n')
        lst[inc] = elmnt
        inc = inc + 1

    # splits each directory line into email and password
    # and checks with the directory if the email and password
    # exist in the directory

    for line in lst:
        match = False
        info_separator = line.split(" ")
        if email_info == info_separator[0] and pass_info == info_separator[1]:
            match = True
            break

    # if Sign In data matches, display Sign Up GUI
    if (match == True):
        Label(screen, text="Sign In Successful", fg="green", font=("calibri", 11)).place(x=15, y=200)
        file.close()
        # print("success")
        global screen_sp
        screen_sp = Toplevel(screen)
        screen_sp.geometry("700x400")
        screen_sp.title("Python Form 2")
        heading_sp = Label(screen_sp,
                           text="Email Input",
                           bg="beige",
                           fg="black",
                           width="700",
                           font=("Times", 25))
        heading_sp.pack()
        # takes input from Sign Up GUI window
        email_sp_text = Label(screen_sp, text="Email: ", font=("Times", 16))
        email_sp_text.place(x=15, y=60)
        password_sp_text = Label(screen_sp, text="Password: ", font=("Times", 16))
        password_sp_text.place(x=15, y=140)
        confirm_sp_password_text = Label(screen_sp, text="Confirm Password: ", font=("Times", 16))
        confirm_sp_password_text.place(x=15, y=220)

        global email_sp
        global password_sp
        global confirm_sp_password
        global email_sp_text_entry
        global password_sp_text_entry
        global confirm_sp_password_text_entry
        email_sp = StringVar()
        password_sp = StringVar()
        confirm_sp_password = StringVar()

        email_sp_text_entry = Entry(screen_sp, textvariable=email_sp, width="50")
        password_sp_text_entry = Entry(screen_sp, textvariable=password_sp, width="50")
        confirm_sp_password_text_entry = Entry(screen_sp, textvariable=confirm_sp_password, width="50")

        email_sp_text_entry.place(x=15, y=100)
        password_sp_text_entry.place(x=15, y=180)
        confirm_sp_password_text_entry.place(x=15, y=260)

        # Sign Up button once clicked checks Sign Up info
        register_sp = Button(screen_sp,
                              text="Sign Up",
                              width="10",
                              height="1",
                              bg="beige",
                              font=("Times", 16),
                              command=write_data
                              ).place(x=15, y=300)

# checking information from input screen ends

# Displays the Sign In Form
screen = Tk()
screen.geometry("400x250")
screen.title("Python Form")

email_text = Label(text="Email: ", font=("Times", 16))
email_text.place(x=15, y=10)
password_text = Label(text="Password: ", font=("Times", 16))
password_text.place(x=15, y=80)

email = StringVar()
password = StringVar()

email_text_entry = Entry(textvariable=email, width="50")
password_text_entry = Entry(textvariable=password, width="50")

email_text_entry.place(x=15, y=40)
password_text_entry.place(x=15, y=110)

# Sign In Button checks data and opens up Sign Up GUI window
register = Button(screen,
                  text="Sign In",
                  width="10",
                  height="1",
                  bg="beige",
                  font=("Times", 16),
                  command=check_info_input)
register.place(x=15, y=150)
screen.mainloop()