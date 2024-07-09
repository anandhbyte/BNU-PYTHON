import re

text = "Hello BCA Students! Welcome to 4th Sem"

# re.match() tries to match a pattern at the beginning of the string.
match = re.match("Hello", text)
print("Match:", match.group() if match else None)

# re.search() searches the string for a match and returns a Match object if there is a match.
search = re.search("BCA", text)
print("Search:", search.group() if search else None)

# re.findall() returns a list containing all matches.
findall = re.findall("[0-9]", text)
print("Findall:", findall)

# re.split() returns a list where the string has been split at each match.
split = re.split("\s", text)
print("Split:", split)

# re.sub() replaces the matches with the text of choice.
sub = re.sub("4th", "Third", text)
print("Sub:", sub)

readkey()