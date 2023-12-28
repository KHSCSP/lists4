# original data https://en.wikipedia.org/wiki/Wikipedia:10,000_most_common_passwords
# the data has been modified


print("\n--- loading the 10,000 most common passwords ---")
f = open('lists4/passwords.txt', "r")
passwords = []
for line in f:
  line = line.strip() # this will remove 'newlines'
  passwords.append(line)
f.close()


print("\n--- what's in the data ---")
print("length", len(passwords))
print("first", passwords[0])
print("last", passwords[-1])
print("a slice", passwords[0:10])




print("\n--- analyzing the data ---")
s = ''
# convert to one long string
for item in passwords:
  s += item.lower()

# create a list of each letter and its frequency
chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
counts = []
for c in chars:
  counts.append([c, s.count(c)])

print("here's each letter and its frequency:", counts)



    
print("\n--- search for an item ---")
choice = 'banana'
while choice[0] != 'q':
  choice = input("\nWhat to look for? q to quit:").lower()
  if choice in passwords:
    place = passwords.index(choice)
    print("found that at position", place)
  else:
    print("that is not in the 10000 most common passwords")



