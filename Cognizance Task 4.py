# Name : Amirthavarshini V (21105)
# ch.en.u4aie21105@ch.students.amrita.edu
# Cognizance club Task -4 Easy level python programming
# This program has all questions in it


c = int(input("Enter the question you want to see : "))

if c==1:
    # Question - 1
    # Program to perform simple addition
    print("Q1 - Write a program to perform addition on two user input numbers.")
    num1 = int(input("Enter Number 1 : "))
    num2 = int(input("Enter Number 2 : "))
    print("The sum of the entered numbers is : ",num1+num2)

elif c==2:
    # Question 2
    # Print the characters at the even index
    print("Q2 - Write a program to accept a string from the user and display characters, that are present at an even index number.")
    ch = input("Enter the string : ")
    print("Characters at even index are : ", ch[::2])

elif c==3:
    # Question 3
    # Write a program that contains 2D list with table of records
    print("Q3 - Write a python program to make a 2-dimensional list that contains represents a table of records")
    # Creating the list
    T = [ ['Roll number', 'Name', 'Marks'], ['1', 'Abc', '90'], ['2', 'Def', '95'], ['3', 'Ghi', '85']]
    for j in T:
        print(j)

    # Appending A new record
    new_rec = input("Enter the new record to be added to the list: ")
    T.append(new_rec)
    for i in T:
        print(i)

    # Extracting a record from the table
    rec = int(input("Enter the record that needs to be extracted : "))
    print(T[rec])

elif c==4:
    # Question 4
    # Check if a number is palindrome or not
    print("Q4 - Write a program to check if the given number is a palindrome number.")
    num1 = input("Enter the number : ")
    num2 = num1[::-1]
    if num1 == num2:
        print("True")
    else:
        print("False")
        
elif c==5:
    # Question 5
    # Print the pattern
    print("Q5 - Print the pattern.")
    r = int(input("Enter the number of rows : "))
    k = 0
    for i in range(0, r+1):
        for k in range (1, (r-i)+1):
            print(end = " ")
        for j in range(0, i):
            print("*", end=" ")
        print("\n")

else:
    print("Choice invalid. Choose between 1-5 only")

