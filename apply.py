f = open("u11lists4\pi_digits.txt", "r")  # open the file for reading
pi = f.read() # read the data into one long string
f.close() # close the file to release memory

print("\n--- part 1, working with a string ---")
# print a slice of the 'pi' variable (maybe 30 digits)


# what type of data do we have? (print the type of 'pi')


# remove any unwanted characters (spaces, newlines, decimals)
# it should look like this when finished: 3141592653589793238462643383279


# how many digits do we have? (what is the length of the variable?)



# how many zeros? (use the count function)



# we need to count how many times each digit appears
# make a list of tuples where each tuple is (digit, count(digit))




# once your program is working, change the file at the top to "pi_million_digits.txt" and run your code again
# YOU MAY NEED TO COMMENT OUT SOME PREVIOUS PRINT STATEMENTS



# search for your birthday in the digits of pi. where is it located?
# example: mmdd or mmddyy or mmddyyyy



#---------------------------------------------------
print("\n\n---- part 2, working with a list of integers ---")
# ---SWITCH BACK TO THE "SHORT" VERSION OF PI---
# convert your string into a list of integers
# your variable should look like this:
# [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9]
# hint: this will require you to loop through each item in your string and append the integer version of that item to a list




# how many zeros?




# count how many digits are less than 5 (this will require a loop)




# we need to count how many times each digit appears
# make a list of tuples where each tuple is (i, count(i))



# once your program is working, change the file to "pi_million_digits.txt" and run your code again



