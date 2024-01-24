
def get_pi(filename):
    # read in the file (into a list of strings)
    with open(filename) as f:
        lines = f.readlines()
    # strip of new lines and whitespace
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    return pi_string
# -- do not edit above this line ---



# the 'short' version of pi
pi_string = get_pi('u11lists4/pi_digits.txt')

# more digits!! use this later
#pi_string = get_pi('u11lists4/pi_million_digits.txt')





# fun stuff
# how many digits do we have?
print("there are", len(pi_string), 'digits')
print(pi_string[:50])


# where is your birthday?
if '012345' in pi_string:
    print('found it at position', pi_string.index('012345'))



# count occurrances of each digit
counts = [0,0,0,0,0,0,0,0,0,0]
for letter in pi_string[2:]:
    digit = int(letter)
    counts[digit] += 1

print(counts)



# print the 'pi' variable


# what type of data do we have? (print the type of 'pi')


# remove any unwanted characters (spaces, newlines, decimals)
# it should look like this when finished: 3141592653589793238462643383279


# how many digits do we have? (what is the length of the variable?)



# how many zeros? (use the count function)



# we need to count how many times each digit appears
# make a list of tuples where each tuple is (digit, count(digit))
# hint: loop using the range function, then you'll need to 'count(str(i))'




# once your program is working, change the file at the top to "pi_million_digits.txt" and run your code again
# YOU MAY NEED TO COMMENT OUT SOME PREVIOUS PRINT STATEMENTS



# search for your birthday in the digits of pi. where is it located?




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


