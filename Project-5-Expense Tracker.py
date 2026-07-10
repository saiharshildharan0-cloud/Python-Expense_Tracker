#Python Project-Expense Tracker
print('''Python Expense Tracker
-------------------------------------------------------
Welcome to Python Expense Tracker!!! A place, where you
can keep a track of your expenses and calculate your
total spending.

You would need to provide the tracker
with 4 inputs:-
A)Date-The date on which you spent a certain amount.
B)Category-Under which category (for example, food,
           essentials, shopping, etc.), you spent.
C)Description-What exactly did you spend on under that
              category.
D)Amount-How much did you spend for that item.

You can choose any one of the following
options from the menu:-
MENU
====
1)Add expense/expenses
2)View expenses
3)View total expense
4)Search expense by category
5)Exit''')

#Functions for each of the given options in the menu.
import csv #Expenses stored in a CSV file for which the csv module is imported.
def Add():
    with open("Expenses.csv","a",newline="") as file:
        writer=csv.writer(file)
        no_of_expenses=int(input("How many expenses would you like to add?:"))
        for i in range(0,no_of_expenses):
            date = input(f"Enter date {i+1}: ")
            category = input(f"Enter category {i+1}: ")
            desc = input(f"Enter description {i+1}: ")
            amount = float(input(f"Enter amount {i+1}: "))
            writer.writerow([date,category,desc,amount])
def View():
    with open("Expenses.csv","r",newline="") as file:
        reader=list(csv.reader(file))
        for j in reader:
            print(j) #Showing the expenses along with the headers one by one.
def Total():
    with open("Expenses.csv","r",newline="") as file:
        reader=list(csv.reader(file))
        amounts=list() #Stores the amounts of all descriptions.
        for row in reader[1:]:
            amounts.append(float(row[3]))
        print("Total expense is:",sum(amounts))
def Search():
    with open("Expenses.csv","r",newline="") as file:
        reader=list(csv.reader(file))
        cat=input("Enter category to be searched:")
        for l in reader[1:]:
            if l[1]==cat:
                print(l)
def Exit():
    print("Exited succesfully!!!")

while True:
    choice=input("Enter your choice from the given menu:")
    if choice=="1":
        Add()
    elif choice=="2":
        View()
    elif choice=="3":
        Total()
    elif choice=="4":
        Search()
    elif choice=="5":
        Exit()
        break


    
        
    
            
    
    
            
        
    
    
        


