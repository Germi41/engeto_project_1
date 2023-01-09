"""
projekt1.py: první projekt do Engeto Online Python Akademie
author: David Germ
email: david.germ@kiwi.com
discord: GermiCZ#2828
"""

separator = (40 * '-')
text_counter = 0
words_counter = 0
uppercase_words = 0
lowercase_words = 0
isnumeric_words = 0
titlecase_words = 0
sum = 0
words_len = dict()
clean_words = list()
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pas123"
}
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''']

# LOGIN:

username = input("username:")
if username in users.keys():
    password = input("password:")
    if password in users.get(username):
        print(separator, sep="\n")
        print(f"Welcome to the app, {username.upper()}.", sep="\n")
    else:
        print("Wrong password. Terminating the program...")
        exit()
else:
    print("This user doesn't exists. Terminating the program...")
    exit()

# TEXT CONTROL

if not TEXTS:
    print("We have 0 texts to be analyzed. Terminating the program...")
    exit()
else:
    for text in TEXTS:
        text_counter = text_counter + 1

# TEXT SELECTION AND PREPARATION FOR ANALYSIS

print(f"We have {text_counter} texts to be analyzed.")
print(separator, sep="\n")
text_selected = input(f"Enter a number btw. 1 and {text_counter} to select: ")

if text_selected.isnumeric() is False:
    print("You did not enter the number. Terminating the program...")
    exit()
elif int(text_selected) not in range(1, text_counter + 1):
    print("This text doesn't exist. Terminating the program...")
    exit()
else:
    print(separator, sep="\n")
    text_words = TEXTS[int(text_selected)-1].split()
    for word in text_words:
        clean_words.append(word.strip(",;:.?!"))

# TEXT ANALYSIS

for word in clean_words:
    words_counter = words_counter + 1
    if word.isnumeric():
        isnumeric_words = isnumeric_words + 1
        sum = sum + int(word)
    elif word.islower():
        lowercase_words = lowercase_words + 1
    elif word.isupper():
        uppercase_words = uppercase_words + 1
    elif word.istitle():
        titlecase_words = titlecase_words + 1

# PRINT RESULTS

print(f"There are {words_counter} words in the selected text.")
print(f"There are {titlecase_words} titlecase words.")
print(f"There are {uppercase_words} uppercase words.")
print(f"There are {lowercase_words} lowercase words.")
print(f"There are {isnumeric_words} numeric strings.")
print(f"The sum of all numbers is {sum}.")
print(separator)

# TEXT OCCURRENCES

for word in clean_words:
    if len(word) not in words_len:
        words_len[len(word)] = 1
    else:
        words_len[len(word)] = words_len[len(word)] + 1

# PRINT OCCURRENCES

print(f"LEN|" + "OCCURRENCES".center(max(words_len.values())+2) + "|NR.")
print(separator)
for (key, value) in sorted(words_len.items()):
    adj_key = str(key).rjust(3)
    occurs = value * "*"
    print(f"{adj_key}|" + occurs.ljust(max(words_len.values())+2) + f"|{value}")

# S tim poslednim printem jsem si moc rady nevedel
# +2 je tam proto, aby mezery sedeli s prikladem v zadani projektu
# snad nevadi, ze je to v AJ, pracuji jako QA 3 roky a nejsem na CJ zvykly v kodu
