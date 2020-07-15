from ClassLoan import *
from tkinter import *
from tkinter import messagebox

# Create root window
root = Tk()

# Change the color scheme of the background
purple = "#CCCCFF"
root.config(background=purple)

# Create the labels
font = ("Comic Sans SF", 8)
l1 = Label(root, text="Loan Amount", fg="black", font=font, background=purple, anchor="center")
l2 = Label(root, text="Years of Payments", fg="black", font=font, background=purple, anchor="center")
l3 = Label(root, text="Interest Rate (%)", fg="black", font=font, background=purple, anchor="center")
l4 = Label(root, text="Monthly Payment", fg="black", font=font, background=purple, anchor="center")

# Place the labels in a Grid
l1.grid(row=0, padx=(10, 0))
l2.grid(row=1, padx=(10, 0))
l3.grid(row=2, padx=(10, 0))
l4.grid(row=3, padx=(10, 0))

# Create Variables for Initial Entries and Calculation Entry
e1 = Entry(root, justify="center", cursor="umbrella")
e2 = Entry(root, justify="center", cursor="umbrella")
e3 = Entry(root, justify="center", cursor="umbrella")
monthly_payment = Entry(root, justify="center", disabledbackground="gray80", cursor="no", state=DISABLED)

# Place the Entries in a Grid
e1.grid(row=0, column=1, columnspan=2, padx=(10, 10), pady=10, ipady=2)
e2.grid(row=1, column=1, columnspan=2, padx=(10, 10), pady=10, ipady=2)
e3.grid(row=2, column=1, columnspan=2, padx=(10, 10), pady=10, ipady=2)
monthly_payment.grid(row=3, column=1, columnspan=2, padx=(10, 10), pady=10, ipady=2)


def custom_entry():

    # Create Custom Labels
    l5 = Label(root, text="Custom Amount", fg="white", font=font, background=grey)
    l6 = Label(root, text="Custom Duration", fg="white", font=font, background=grey)
    l7 = Label(root, text="Monthly Payment For Remaining Years", fg="white", font=font, background=grey)
    l8 = Label(root, text="Total Years To Complete Loans", fg="white", font=font, background=grey)

    # Set Positions of Custom Labels
    l5.grid(row=4, pady=20, padx=(10, 0))
    l6.grid(row=5, pady=4, padx=(10, 0))
    l7.grid(row=6, pady=4, padx=(10, 0))
    l8.grid(row=7, pady=4, padx=(10, 0))

    # Create Variables for Custom Entries and Custom Calculation Entry
    global e4  # Global so other functions can access it
    e4 = Entry(root, justify="center", cursor="pencil")
    global e5
    e5 = Entry(root, justify="center", cursor="pencil")
    global custom_payment
    custom_payment = Entry(root, disabledbackground="gray80", cursor="no", state=DISABLED)
    global remaining_years
    remaining_years = Entry(root, disabledbackground="gray80", cursor="no", state=DISABLED)

    # Set Positions of Custom Labels
    e4.grid(row=4, column=1, columnspan=2, padx=(10, 10), pady=10, ipady=2)
    e5.grid(row=5, column=1, columnspan=2, padx=(10, 10), pady=10, ipady=2)
    custom_payment.grid(row=6, column=1, columnspan=2, padx=(10, 10), pady=10, ipady=2)
    remaining_years.grid(row=7, column=1, columnspan=2, padx=(10, 10), pady=10, ipady=2)

    # Allow Button to be Pressed After the Function has been Called
    b2.config(state=NORMAL)


def calc(arg):

    # Check for Errors in the First Entry
    try:
        user_amount = float(e1.get())
    except ValueError:
        messagebox.showerror("Invalid Entry", "Input Proper Value For The Loan Amount")
        return

    # Check for Errors in the Second Entry
    try:
        global user_age
        user_age = float(e2.get())
    except ValueError:
        messagebox.showerror("Invalid Entry", "Input Proper Value For The Years of Payments")
        return

    # Check for Errors in the Third Entry
    try:
        user_interest = float(e3.get())
    except ValueError:
        messagebox.showerror("Invalid Entry", "Input Proper Value For The Interest Rate")
        return
    if user_interest > 100:
        messagebox.showerror("Invalid Entry", "Interest Rate Cannot Be Over 100")
        return

    # Calculate Loan
    global user_loan  # Global variable so other functions can access it
    user_loan = Loan(user_amount, user_interest, user_age)
    user_monthly_payment = user_loan.loan_calculation()

    # Allow Entry to be Changed and Disable After it Has Been Changed
    arg.config(state=NORMAL)
    arg.delete(0, 'end')
    arg.insert(0, str(user_monthly_payment))
    arg.config(state=DISABLED)


def custom_calc(arg1, arg2):

    # Check for Errors in Custom Entry 1
    try:
        custom_amount = float(e4.get())
    except ValueError:
        messagebox.showerror("Invalid Entry", "Input Proper Value for Custom Amount")
        return

    # Check for Errors in Custom Entry 2
    try:
        custom_duration = float(e5.get())
    except ValueError:
        messagebox.showerror("Invalid Entry", "Input Proper Value for Custom Duration")
        return

    if custom_duration >= user_age:
        messagebox.showerror("Invalid Entry", "Custom Duration Cannot Equal or be Larger than to Years of Payment")
        return

    # Complete Calculations
    custom_loan = CustomLoan(user_loan, custom_amount, custom_duration)
    custom_loan_payment = custom_loan.custom_calculation(user_loan)

    # Allow Custom Entry 1 to be Changed and Disable After it Has Been Changed
    arg1.config(state=NORMAL)
    arg1.delete(0, 'end')
    arg1.insert(0, str(custom_loan_payment[1]))
    arg1.config(state=DISABLED)

    # Allow Custom Entry 2 to be Changed and Disable After it Has Been Changed
    arg2.config(state=NORMAL)
    arg2.delete(0, 'end')
    arg2.insert(0, str(custom_loan_payment[0]))
    arg2.config(state=DISABLED)


# Create Menu
menu = Menu(root)
root.config(menu=menu)
options = Menu(menu)
menu.add_cascade(label="Options", menu=options)
options.add_command(label="Custom payments", command=custom_entry)

# Create Buttons
b1 = Button(root, text="Calculate", command=lambda: calc(monthly_payment))
b1.grid(row=8, column=1, pady=10)
b2 = Button(root, text="Custom", command=lambda: custom_calc(custom_payment, remaining_years))
b2.config(state=DISABLED)
b2.grid(row=8, column=2, pady=10)

# Set so Program doesn't Terminate Until the Program is Exited
mainloop()

