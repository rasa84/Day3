# STRINGAI
import random
import re
import string

print("****************************************")
print("Pirma uzduotis")

name = "Petras"
last_name = "Petraukas"
shorterSting = name if len(name) < len(last_name) else last_name

print(f"Trumpesnis stringas {shorterSting}")

print("****************************************")
print("Antra uzduotis")

name = "Petras"
last_name = "Petraukas"
a = 1 * 9

print(f"Vardas {name.upper()}")
print(f"Pavarde {last_name.lower()}")

print("****************************************")
print("Trecia uzduotis")

name = "Petras"
last_name = "Antainaitis"
initials = name[0] + last_name[0]

print(f"Inicialai {initials}")

print("****************************************")
print("Ketvirta uzduotis")

name = "Petras"
last_name = "Antainaitis"
mutant = name[-3:] + last_name[-3:]

print(f"Trys paskutinės vardo ir pavardės raidės: {mutant}")

print("****************************************")
print("Penkta uzduotis")
text = "An American in Paris"
letter_a = re.compile("a", re.IGNORECASE)
text2 = letter_a.sub("*", text)
# text.replace('a', '*')

print(f"'a' raides pakeistos žvaigždutėm: {text2}")

print("****************************************")
print("Sesta uzduotis")

text1 = "An American in Paris"
text2 = "Breakfast at Tiffany's"
text3 = "2001: A Space Odyssey"
text4 = "It's a Wonderful Life"
vowels = re.compile('[aeiou]', re.IGNORECASE)
mod_text1= vowels.sub('',text1)
mod_text2= vowels.sub('',text2)
mod_text3= vowels.sub('',text3)
mod_text4= vowels.sub('',text4)

print(f"Ištrintos balsės: {mod_text1}")
print(f"Ištrintos balsės: {mod_text2}")
print(f"Ištrintos balsės: {mod_text3}")
print(f"Ištrintos balsės: {mod_text4}")

print("****************************************")
print("Septinta uzduotis")

starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"
num = re.findall(r'\d+', starWars)

print(starWars)
print(f"Numeris: {num[0]}")

print("****************************************")
print("Astunta uzduotis")

text = "Don't Be a Menace to South Central While Drinking Your Juice in the Hood"
words = text.split()
count = 0
for word in words:
    if len(word) <= 5:
        count += 1
print(f"Žodžių iš viso: {len(words)}. Žodžių trumpesnių arba lygių nei 5 raidės skaičius: {count}")

text = "Tik nereikia gąsdinti Pietų Centro, geriant sultis pas save kvartale"
words = text.split()
count = 0
for word in words:
    if len(word) <= 5:
        count += 1
print(f"Žodžių iš viso: {len(words)}. Žodžių trumpesnių arba lygių nei 5 raidės skaičius: {count}")

print("****************************************")
print("Devinta uzduotis")

# random_text = ''.join(random.choices(string.ascii_lowercase, 3))
# random_text = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
random_text = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3))

print(f"Generated random text: {random_text}")

print("****************************************")
print("Desimta uzduotis")

text1 = "Be a Menace to South Central While Drinking Your Juice in the Hood"
text2 = "Tik nereikia gąsdinti Pietų Centro, geriant sultis pas save kvartale"
text = text1 + " " + text2
words = text.split()
sample = random.sample(words, 10)

print(f"Pirmas sakinys su atsitiktine tvarka sugeneruotais žodžiais: {sample}")
