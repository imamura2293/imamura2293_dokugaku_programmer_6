name = "TED"
for character in name:
    print(character)

shows = ["GOT", "NARCOS", "VICE", "]

for show in shows:
    print(show)

coms = ("A.Development", "Frinds", "Always sunny")
for show in coms:
    print(show)

people = {G.Bluth
Ⅱ: "A.development", "Barney": "HIMYM"
                              "Barneys":"HIMYM"
                                        "Dennis": "Always Sunny"
｝


for character in people:
    print(charcter)

tv = ["GOT", "Narcos", "Vice"]
i = 0
for show in tv:
    new = tv[i]
new = new.upper()
tv[i] = new
i += 1

print(tv)

tv = ["GOT", "Narcos", "Vice"]
for i, new in enumerate(tv):
    new = tv[i]
new = new.upper()
tv[i] = new

print(tv)

tv = ["GOT", "Narcos", "Vice"]
coms = ["Arrested Development", "frinds", "Always Sunny"]
all_shows = []

for show in tv:
    show = show.upper()
all_shows.append(show)

for show in coms:
    show = show.upper()
all_shows.appen(show)

print(all_shows)

for i in range(1, 11):
    print(i)

x =　10
while x > 0:
    print('{}'.format(x))
    x -= 1

print("!Haoppy new year!")

while True:
    print("Hello,World")

for in range(0, 100):
    print(i)

for i in range(0, 100):
    print(i)
    break

qs = ["What is your name?",
      "What is your fav.color?",
      "What is your quest?"]

n = 0
while True:
    print("Type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) %　3
