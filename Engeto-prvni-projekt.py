'''
author =
'''
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
garpike and stingray are also present.'''
]

# uvod
oddelovac = "-" * 40
jmeno = input("Username: ")
heslo = input("Password: ")

if jmeno == "bob" and heslo == "123":
  print(oddelovac,
        f"Welcome to the app, {jmeno}",
        "We have 3 texts to be analyzed.",
        oddelovac, sep = "\n")
elif jmeno == "ann" and heslo == "pass123":
  print(oddelovac,
        f"Welcome to the app, {jmeno}",
        "We have 3 texts to be analyzed.",
        oddelovac, sep = "\n")
elif jmeno == "mike" and heslo == "password123":
  print(oddelovac,
        f"Welcome to the app, {jmeno}",
        "We have 3 texts to be analyzed.",
        oddelovac, sep = "\n")
elif jmeno == "liz" and heslo == "pass123":
  print(oddelovac,
        f"Welcome to the app, {jmeno}",
        "We have 3 texts to be analyzed.",
        oddelovac, sep = "\n")

else:
  print("unregistered user, terminating the program..")
  quit()

# vyber
vyber = input("Enter a number btw. 1 and 3 to select: ")
if vyber == "1":
  text = TEXTS[0]
elif vyber == "2":
  text= TEXTS[1]
elif vyber == "3":
  text = TEXTS[2]
elif (vyber.isalpha()):
  print("Enter only a number btw. 1 and 3, terminating the program..")
  quit()
else:
  print("Enter only a number btw. 1 and 3, terminating the program..")
  quit()

print(oddelovac)

# statistiky
vyber_textu = text.split()

cista_slova = [ciste_slovo.strip(".,") for ciste_slovo in vyber_textu]

vysledek_velka = [slovo for slovo in cista_slova if slovo.istitle()]
vysledek_vsechna_velka = [slovo for slovo in cista_slova if slovo.isupper()]
vysledek_mala = [slovo for slovo in cista_slova if slovo.islower()]
cisla = [int(slovo) for slovo in cista_slova if slovo.isnumeric()]

print(f"""
There are {len(cista_slova)} words in the selected text.
There are {len(vysledek_velka)} titlecase words.
There are {len(vysledek_vsechna_velka)} uppercase words.
There are {len(vysledek_mala)} lowercase words.
There are {len(cisla)} numeric strings.
The sum of all the numbers {sum(cisla)}
""")

# cetnost slov v textu
delka_vsech_slov = []

for word in cista_slova:
  delka_slova = len(word)
  delka_vsech_slov.append(delka_slova)

cetnost = dict((x,delka_vsech_slov.count(x)) for x in set(delka_vsech_slov))

# zapis tabulky
len = "LEN"
occurences = "OCCURENCES"
nr = "NR."
print(oddelovac)
print(f"{len}|{occurences: ^20}|{nr}")
print(oddelovac)

prevod_slovniku = cetnost.items()
for _, hodnota in enumerate(sorted(prevod_slovniku)):
  pocet_znaku = hodnota[1]
  znaky = pocet_znaku * "*"
  print(f"{hodnota[0]: >3}|{znaky: <20}|{hodnota[1]}", sep = "\n")