#---------------------------------------------------#
# Title: Homework 5
# Dev: Catherine Warren
# Date: 2013-07-21
# Desc: ToDo List using dictionary
#---------------------------------------------------#

#-- Data --#
# declare variables and constants

# ToDoDict is the dictionary of tasks and their priorities. I'm creating a blank one first:

ToDoDict = {}

# Then I will fill it with the contents of the ToDo.txt file:

text_file = open("C:\\_PythonClass\\ToDo.txt", "r")
for line in text_file:
    strData = line # readline() reads a line of the data
    ToDoItem = (strData.split(",")[0]).strip(), (strData.split(",")[1]).strip() #splits apart the existing data into a key-value pair
    ToDoDict = {ToDoItem[0]: ToDoItem[1]}
    # show the user existing tasks
    print(ToDoDict.items())


# next, ask the user what s/he wants to do

print('1. Add task')
print('2. Remove task')
print('3. Save tasks to file')
menu_choice = float(input("\nChoose an option: "))

while menu_choice != 0:
    try:
        # to add a task
        if menu_choice == 1:
            ToDoItem = str(input("Add a task: "))
            priority = float(input("\nAssign it a priority from 1 (most important) to 5 (least important): "))
            ToDoDict[ToDoItem] = priority
            print("\n", ToDoItem, "has been added.")
            print("\n1. Add task")
            print("2. Remove task")
            print("3. Save tasks to file")
            menu_choice = float(input("\nChoose an option: "))

        # to delete a task
        elif menu_choice == 2:
            ToDoItem = input("What task do you want to delete? ")
            if ToDoItem in ToDoDict:
                del ToDoDict[ToDoItem]
                print("\n", ToDoItem, " has been deleted.")
                menu_choice = float(input("\nChoose an option: "))
            else:
                print("\nAn error occurred.")
                print("\n1. Add task")
                print("2. Remove task")
                print("3. Save tasks to file")
                menu_choice = float(input("\nChoose an option: "))

        # to save the tasks to file
        elif menu_choice == 3:
            import json
            json.dump(ToDoDict, open("C:\\_PythonClass\\ToDo.txt", "w"))
            print("Data was saved!")
            break

    except:
        print("\nAn error occurred.")
        print("\n1. Add task")
        print("2. Remove task")
        print("3. Save tasks to file")
        menu_choice = float(input("\nChoose an option: "))

if menu_choice == 0:
    print("Goodbye.")
