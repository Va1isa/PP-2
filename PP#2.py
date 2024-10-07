i = 0 #Initializes i with 0

while i < 10: #The loop will end once i reaches 10
    if i % 2 == 0:
        print(i, 'even') #If there is no remainder then the number should be even
    else:
        print(i, 'odd') #If the remainder is 1 then the number should be odd

    i = i + 1 #Add 1 to i so that it will increase, otherwise it will be an infinite loop

#The output will count to 9 and say which numbers are even or odd
