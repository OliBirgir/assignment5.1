#The algorithm for this assignment is like this:
#user tells us the length of the sequence, which means that we will print out x amount of numbers in a sequence.
#the code is supposed to print out all three numbers below.
# for example: 1,2,3,(3+2+1) = 6, (6+3+2) = 11....
# you will need three numbers. a_int, b_int and c_int and a counter, which counts the input
# while the input is more or the same as the counter, it should summarize a_int, b_int and c_int.

n = int(input("Enter the length of the sequence: "))
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


    

