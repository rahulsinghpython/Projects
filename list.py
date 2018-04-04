menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])

for meal in menu:
    if not "spam" in meal:
        print(meal)
        for ingrediants in meal:
            print(ingrediants)