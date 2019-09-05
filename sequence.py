#The algorithm for this assignment is like this:
#user tells us the length of the sequence, which means that we will print out x amount of numbers in a sequence.
#the code is supposed to print out all three numbers below.
# for example: 1,2,3,(3+2+1) = 6, (6+3+2) = 11....
# you will need few integers. a_int, b_int and c_int, sum and a counter, which counts the input
# while the input is more or the same as the counter, it should summarize a_int, b_int and c_int.
#print out the sum and add 1 to the counter
#While a_int is more or the same as two, the number c will be the same as b, which leads to correct printing for 3
#then b_int becomes a_int and the a_int becomes the sum.
n = int(input("Enter the length of the sequence: ")) # Do not change this line
a_int = 1
b_int = 0
c_int = 0
counter = 0
sum_int = 0
while n>counter:
    sum_int = (a_int + b_int + c_int)
    print(sum_int)
    counter+=1
    if a_int >= 2:
        c_int = b_int
    b_int = a_int
    a_int = sum_int

