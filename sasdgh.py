
from random import randint, choice


# ---------------------------------
name = input('Podaj imie twojego bohatera: ')
life = 100
zasoby = 100


# def----def------def-------def----------

def wydobycie():
    return randint(1,6)

# ---------------------------------------
def dynamit():
    global zasoby
    if zasoby < 10:
        print("-"*40)
        print("Nie masz wystarczającej ilości TNT!")
        return 0
    zasoby -= 10
    return randint(13, 20)

#------------------------------------------

def wybierz_sposob():
    print('a/A - Wykonaj Normalne Wydobycie')
    print('b/B - Użycie Dynamitu!')
    print('c/C - Powrót Na Górę!')                          # pomyśl nad questami
    co = input().upper()
    if co == 'A':
        return wydobycie()
    elif co == 'B':
        return dynamit()
    elif co == 'C':
        return powrot_na_gore()
    else:
        print("Nie wybrano akcji")
        return 0
# -----------------------------------------
def spanie():
    global life
    if life > 49:
        print("-"*40)
        print("Nie jesteś zmęczony")
        return 0
    life += 70                                               # nie działa +
# -----------------------------------------

def TNT_branie():
    global zasoby
    if zasoby < 51:
        print("-"*40)
        print("Bierz TNT!")
        return 0
    zasoby +=50                                                 # nie działa +
    return randint(13, 20)

# ------------------------------------------
def powrot_na_gore():
    print('a/A - Idź do domu wypocząć')
    print('b/B - Idź uzupoełnić dynamit')
    print('c/C - Wróć na dół')
    abc = input().upper()
    if abc == "A":
        return spanie
    elif abc == 'B':
        return TNT_branie()
    elif abc == 'C':
        return wydobycie()
    else:
        print("Nie wybrano akcji")
        return 0

# ores---------------------------------------
def random_ores():
    opponents = [
        ["Kamień", 10, 1, 0],
        ["Ruda Żelaza", 20, 4, 0]
    ]
    return choice(opponents)


# --------------------------------------------
liczba_wykopanych__rud = 0


while life > 0:
    opponent = random_ores()
    print("-"*40)


    while opponent[1] > 0 and life > 0:
        print(f"{name} wydobywa teraz {opponent[0]}")
        print(f"Surowiec ma {opponent[1]} HP i zadaje Ci {opponent[2]} punkty wycięczenia")
       
        life -= opponent[2]
        if life <= 0:
            break


        print(f"Masz {life} Punktów wycięczenia i {zasoby} dynamtu")
        atak = wybierz_sposob()
        opponent[1] -= atak
        print(f"Zadałeś {atak} obrażeń")


    if opponent[1] <= 0:
        print('Wydobyłeś Rudę!!!')
        liczba_wykopanych__rud += 1


print("-"*40)
print("KONIEC GRY!")
print("Umarłeś Z Wykończenia")
print(f"Wykopałeś {liczba_wykopanych__rud} Rud!!!")