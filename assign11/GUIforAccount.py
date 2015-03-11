# module allows user to interact with bank account
# make deposits and withdrawals
# display current balance

import bankAccountClass
from tkinter import *

# create bank account
class AccountGUI:
    # the constructor
    def __init__(self):
        # create the BankAccount object that the GUI will give access to
        self.account = bankAccountClass.BankAccount(0)
        # create the main window and give it a title
        root = Tk()
        root.title('My ATM')
        
        ## create each widget and place it in the main window
        # create labels for initial balance, deposit and withdraw
        self.balance = Label(root,text = 'Enter initial balance').grid(row=0,column=0)
        self.deposit = Label(root,text = 'Enter amount to deposit:').grid(row=2,column=0)
        self.withdraw = Label(root,text = 'Enter amount to withdraw:').grid(row=4,column=0)

        # create entry space for initial balance
        self.balance_entry = Entry(root)
        self.balance_entry.grid(row=0,column=1)

        # create entry space for deposit
        self.deposit_entry = Entry(root)
        self.deposit_entry.grid(row=2,column=1)

        # create entry space for withdraw
        self.withdraw_entry = Entry(root)
        self.withdraw_entry.grid(row=4,column=1)

        # create get button label
        self.button = Button(root,text = 'Display amount balance:',\
                             bg = 'white',\
                             fg = 'red',\
                             command = self.display)
        self.button.grid(row=6, columnspan = 2,sticky = W+E+N+S)

        self.answer = Label(root,text = '')
        self.answer.grid(row=7, rowspan = 2)
   
        # display the main window and start the event processing loop
        root.mainloop()
        
    # define a callback method for each widget that 
    # is supposed to make something happen
    def display(self):
        # get value of initial balance and create account with initial balance
        ini_balance = self.balance_entry.get()
        try:
            ini_balance = float(self.balance_entry.get())
            account = bankAccountClass.BankAccount(ini_balance)
        except ValueError:
            messagebox.showerror("Error","Your initial balance value is incorrect,\nPlease enter again")

        # get deposit and add it to balance    
        deposit = self.deposit_entry.get()
        try:
            deposit = float(self.deposit_entry.get())
            balanceAfterDeposit = account.deposit(deposit)
        except ValueError:
            messagebox. showerror("Error", "Your deposit value is incorrect,\nPlease enter again")

        # get amount to withdraw and subtract it from balance    
        withdraw = self.withdraw_entry.get()
        try:
            withdraw = float(self.withdraw_entry.get())
            balanceAfterWithdraw = account.withdraw(withdraw)
        except ValueError:
            messagebox.showerror("Error", "Your withdraw value is incorrect,\nPlease enter again")

        # get the final balance    
        balance = account.getBalance()
        self.answer.config(text = 'The total balance is '+ str(balance))

#create an instance of the AccountGUI class        
AccountGUI()        

