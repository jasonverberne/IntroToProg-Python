# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Jason Verberne,11/13/22,Added code to complete assignment 5
# Jason Verberne, 11/14/22,Continued adding code to complete assignment 5
# Jason Verberne, 11/15/22, Added additional code for option 3
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
strTask = "" # An input of user task
strPriority = "" # An input of user task priority
count = 1 # An incremental count
strRemoveTask = "" # A capture of user task priority
strChoice3 = "" # A capture of user choice for menu option 3

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open("ToDoList.txt","r")
for row in objFile:
    strData = row.split(",")
    dicRow = {"task":strData[0],"priority":strData[1]}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("""Task | Priority\n===============""")
        for row in lstTable:
            print(row["task"] + " | " + row["priority"].strip())
        print("""===============""")
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Please enter the new task: ")
        strPriority = input("Please enter the task priority: ")
        dicRow = {"task":strTask,"priority":strPriority+"\n"}
        lstTable.append(dicRow)
        print("\nYour Task and Priority have been added")
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strChoice3 = input("""Do you want to remove an item by a [N]umber list or [T]yping the task?
           please type 'N' or 'T': """)
        if strChoice3.lower() == "n":
            print("\nThe current tasks are: ")
            print("""===============""")
            count = 1
            for row in lstTable:
                print(str(count) + ". " + row["task"])
                count += 1
            print("""===============\n""")
            strRemoveTask = input("Enter the number of the task you want to remove: ")
            try:
                del lstTable[int(strRemoveTask) - 1]
                print("\nYour selection has been removed.")
            except:
                print("\n** You must enter a valid number choice! **\n\n-- Returning to main menu --")
            continue
        elif strChoice3.lower() == "t":
            strInput = input("\nWhat task would you like to remove: ")
            count = 0
            for row in lstTable:
                if strInput.lower() == row["task"].lower():
                    strFound = row["task"]
                    del lstTable[int(count)]
                    print("\n'" + strFound + "' was removed from the list.")
                    continue
                count += 1
                if count > len(lstTable) - 1:
                    print("\n'" + strInput + "' was not found and was not removed.")
        else:
            print("\n** You must enter a valid number choice! **\n\n-- Returning to main menu --")
        # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(row["task"] + "," + row["priority"])
        objFile.close()
        print("Your list has been saved")
        continue
        # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        strChoice = input("Are you sure you want to exit? Enter 'Y' or 'N': ")
        if strChoice.lower() == 'y':
            print("\n** You have exited the program **")
            break
        else:
            print("\n-- Returning to main menu --")
            continue

input("\nPrese 'Enter' to continue.")