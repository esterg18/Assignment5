'''num_int = int(input("Input a number: "))    # Do not change this line

max_int = 0

while num_int >= 0:
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))


# Fill in the missing code
print("The maximum is", max_int)'''

n = int(input("Enter the length of the sequence: ")) # Do not change this line



if n == 1:
    print(n)
elif n == 2:
    print(1,2)
elif n == 3:
    print (1,2,3)
else:
    print(1)
    print(2)
    print(3)
    
    
    a=1
    b=2
    c=3
    
    for sequence in range(4, n + 1):
        newest_number = a + b + c
        print(newest_number)
        a = b
        b = c
        c = newest_number
        
        sequence = sequence + 1