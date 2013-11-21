#-------------------------------------------------------------------------------
# Name: Homework 04
# Purpose: Help Students
# Author: RRoot
# Created: 07/12
#-------------------------------------------------------------------------------

# Declare, and note, the variables we are going to use
# objFile = "An object that represents a file"
# strData = "A row of text data from the file"
# tplRow = "A array with 2 elements of data"
# tplTable = "A 'table' of rows"


# When the program starts, load the any data you have in the text file
# called HomeInventory.txt into a 2 dimensional tuple.

# The file must be created first before this will work!
# Let's start with the header data
objFile = open("C:\\_PythonClass\\HomeInventory.txt", "r")#see page 193
strData = objFile.readline()
tplRow = (strData.split(",")[0]).strip(), (strData.split(",")[1]).strip() # divide the data into 2 elements
tplTable = tplRow,

#Now, get all of the other rows
for line in objFile:
 strData = line # readline() reads a line of the data
 tplRow = (strData.split(",")[0]).strip(), (strData.split(",")[1]).strip() # divide the data into 2 elements
 tplTable += tplRow, # now add it to the table
print(tplTable)
objFile.close()


#2.	Ask the user for new entries and store them in the tuple;.
print("Type in a 'Name' and Value for your household items")
print("(Enter 'Done' to quit!)")

while(True):
  strName = str(input("Enter a Name: "))
  if(str(strName).lower() == "done"):
    break
  else:
    strValue = str(input("Enter a Value: "))
    tplRow = (strName, strValue) # divide the data into 2 elements
    tplTable += (tplRow), # now add it to the table

#3.	Ask the user, when the program exits, if they would like
# to save/add the data to a text file called, HomeInventory.txt.
print("Would you like to save your new entries?")
strUserInput = str(input("Enter 'y' or 'n'"))
if(strUserInput == 'y'):
    objFile = open("C:\\_PythonClass\\HomeInventory.txt", "w")
    for row in tplTable:
        objFile.write(str(row[0]) + "," + str(row[1]) + "\n")
    objFile.close()
    print("Data was saved:")
else:
    print("Changes were not saved")


