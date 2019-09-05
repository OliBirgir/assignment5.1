#Make sure that you write up the algorithm before starting to code.
#Then implement the algorithm in Python. Put your algorithmic description as a comment in the program file.
#1Create a line that represents the max integer
#A user inputs an positive integer.
#The algorithm checks if the number you inputed is higher then the max integer.
#If it's higher, the max integer becomes the same number that the user inputted, since it was higher than the max.
max_int = 0
num_int = int(input("Input a number: "))    # Do not change this line

while num_int>0:
    if num_int > max_int:
        max_int =num_int
    num_int = int(input("Input a number: ")) 
print("The maximum is", max_int)    # Do not change this line