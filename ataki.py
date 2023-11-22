from random import randint, choice
print("--------WITAJ-W-MINNING-SYMULATOR-------")
print("-"*40)
print("-------WYKONAJ-WSZYSTKIEJ-ZADANIA-------")
print("-------------BY----WYGRAĆ---------------")
print("-"*40)
# -------------------------------------
MAKSYMALNA_LICZBA_RUND = 115


ZASOB_RUDA = "Ruda Żelaza"
ZASOB_KAMIEN = "Kamień"
ZASOB_RUBIN = "Ruda Rubinu"
ZASOB_ZLOTO = "Złoto"

QUEST_ID_1 = 1
QUEST_ID_2 = 2
QUEST_ID_3 = 3
QUEST_ID_4 = 4
QUEST_ID_5 = 5
QUEST_ID_6 = 6

TRYB_BEZ_RUND = 0
TRYB_Z_RUNDAMI = 1

# -------------te-same-questy-------------------------------

zadania = [
    [QUEST_ID_1, "Wydobądź 10 Kamieni", 10, ZASOB_ZLOTO, 1],
    [QUEST_ID_2, "Wydobądż 5 Rudy Żelaza", 5, ZASOB_ZLOTO, 2],
    [QUEST_ID_3, "Wydobądż 2 złota", 2, None, None],
    [QUEST_ID_4, "Wydobądż 4 Rudy Żelaza", 4, ZASOB_RUBIN, 1],
    [QUEST_ID_5, "Wydobądż 5 Rubinów", 5, ZASOB_ZLOTO, 1],
    [QUEST_ID_6, "Użyj 50 dynamitu", 50, ZASOB_ZLOTO, 1]
]
def sprawdz_czy_quest_jest_zrobiony(quest, liczba_kamieni, liczba_rud):
    if quest is None:
        return False
    if quest[0] == QUEST_ID_1 and quest[2] <= liczba_kamieni:
        return True
    elif quest[0] == QUEST_ID_2 and quest[2] <= liczba_rud:
        return True
    elif quest[0] == QUEST_ID_3 and quest[2] <= liczba_zlota:
        return True
    elif quest[0] == QUEST_ID_4 and quest[2] <= liczba_rud:
        return True
    elif quest[0] == QUEST_ID_5 and quest[2] <= liczba__wykopanych__rubinow:
        return True
    elif quest[0] == QUEST_ID_6 and quest[2] <= liczba_uzytego_dynamitu:
        return True
    return False

# =================questy=zabranie=surowcow==========

def usun_zasoby(quest):
    global liczba_wykopanych__kamieni, liczba_wykopanych__rud, liczba__wykopanych__rubinow
    if(quest[0] == QUEST_ID_1):
        liczba_wykopanych__kamieni -= quest[2]
    elif(quest[0] == QUEST_ID_2 or quest[0] == QUEST_ID_4):
        liczba_wykopanych__rud -= quest[2]
    elif(quest[0] == QUEST_ID_5):
        liczba__wykopanych__rubinow -= quest[2]



# -------dane--------------------------
name = input('Podaj imie twojego bohatera: ')
life = 100
zasoby = 100
biezace_zadanie = None
liczba_rund_od_poczatku = 0
tryb_rozgrywki = 0


# def----def------def-------def----------

def wydobycie():
    return randint(1,6)

# ---------------------------------------
def dynamit():
    global zasoby, liczba_uzytego_dynamitu, biezace_zadanie
    if zasoby < 10:
        print("-"*40)
        print("Nie masz wystarczającej ilości TNT!")
        return 0
    zasoby -= 10
    if biezace_zadanie is not None and biezace_zadanie[0] == QUEST_ID_6:
        liczba_uzytego_dynamitu += 10
    return randint(13, 20)

#--------------------tryb-gry----------------------
def wybierz_tryb_gry():
    global tryb_rozgrywki
    print("Wybierz tryb gry")
    print('1 - Bez ograniczonej liczby rund')
    print('2 - Z ograniczoną liczbą rund')
    co = input()
    if(co == '1'):
        print("Wybrano tryb bez rund")
        tryb_rozgrywki = TRYB_BEZ_RUND
    elif(co == '2'):
        print("Wybrano tryb z rundami")
        tryb_rozgrywki = TRYB_Z_RUNDAMI
    else:
        print("Wybrano zły tryb rozgrywki")
        wybierz_tryb_gry()

# --------narmalna-konsola----------

def wybierz_sposob():
    print('a/A - Wykonaj Normalne Wydobycie')
    print('b/B - Użycie Dynamitu!')
    print('c/C - Powrót Na Górę!')
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
        print("Nie jesteś zmęczony!")
        return 0
    life += 70
    return 0
# -----------------------------------------

def TNT_branie():
    global zasoby
    if zasoby < 51:
        print("-"*40)
        print("Bierz TNT!")
        zasoby += 50
        return 0
    return randint(13, 20)

# -------------------------------------------
# dół
# -----------------------------------------

def zabierz_zadanie():
    global biezace_zadanie
    if biezace_zadanie != None:
        print("Nie możesz jednocześnie podjąc dwóch zadań")
        return 0
    biezace_zadanie = quests()
    return 0

# ---------------------------------------------------------

def opusc_quest():
    global biezace_zadanie
    global zadania
    if biezace_zadanie is None:
        return 0
    zadania.append(biezace_zadanie)
    biezace_zadanie = None
    print("-" * 40)
    print("Opuściłeś zadanie!!!")
    print("-" * 40)
    return 0

# ----------------------------------------------------

def pokaz_dostepne_zadania():
    print("-"*40)
    global zadania
    for quest in zadania:
        print(quest[1])
        print("-"*40)
    return 0

# ----------------------------------------------
def powrot_na_gore():
    print('a/A - Idź do domu wypocząć')
    print('b/B - Idź uzupoełnić dynamit')
    print('c/C - Wróć na dół')
    print('q/Q - Przystąp do zadania')
    print('o/O - Porzuć zadanie')
    print('s/S - Pokaż zadania')
    abc = input().upper()
    if abc == "A":
        return spanie()
    elif abc == 'B':
        return TNT_branie()
    elif abc == 'C':
        return wydobycie()
    elif abc == 'Q':
        return zabierz_zadanie()
    elif abc == 'O':
        return opusc_quest()
    elif abc == 'S':
        return pokaz_dostepne_zadania()
    else:
        print("Nie wybrano akcji")
        return 0


# --------Z-A-D-A-N-I-A------------------
def quests():
    global zadania
    wybrane_zadanie = choice(zadania)
    zadania.remove(wybrane_zadanie)
    return wybrane_zadanie



def nagroda(quest):
    global liczba_zlota, liczba__wykopanych__rubinow
    resource = quest[3]
    reward = quest[4]
    if(resource == ZASOB_ZLOTO):
        print(f"Otrzymano nagrode {ZASOB_ZLOTO} {reward} szt")
        liczba_zlota += reward
    elif(resource == ZASOB_RUBIN):
        print(f"Otrzymano nagrode {ZASOB_RUBIN} {reward} szt")
        liczba__wykopanych__rubinow += reward




# ores---------------------------------------
def wylosuj_przeciwnika():
    opponents = [
        ["Kamień", 10, 1, 0],
        ["Ruda Żelaza", 20, 4, 0],
        ["Ruda Rubinu", 35, 8, 0]
    ]
    return choice(opponents)


# ----------dane----------------------------------
liczba_wykopanych__rud = 0
liczba_wykopanych__kamieni = 0
liczba__wykopanych__rubinow = 0
liczba_zlota = 0
liczba_wykonanych__zadan = 0
liczba_uzytego_dynamitu = 0

# -----kontynuacja-rzeczy--------------
def czy_kontuowac_gre():
    global life, liczba_rund_od_poczatku
    return (life > 0 and (tryb_rozgrywki == TRYB_BEZ_RUND or liczba_rund_od_poczatku < MAKSYMALNA_LICZBA_RUND)
            and czy_jest_nie_wykonane_zadnie())


def czy_jest_nie_wykonane_zadnie():
    global biezace_zadanie, zadania
    return (len(zadania) > 0 or (len(zadania) == 0 and biezace_zadanie is not None))


def sprawdz_quest():
    global biezace_zadanie,liczba_wykonanych__zadan
    if (sprawdz_czy_quest_jest_zrobiony(biezace_zadanie, liczba_wykopanych__kamieni, liczba_wykopanych__rud)):
        print(f"Wykonałeś zadanie: {biezace_zadanie[1]}")
        usun_zasoby(biezace_zadanie)
        nagroda(biezace_zadanie)
        liczba_wykonanych__zadan += 1
        biezace_zadanie = None
    return len(zadania) == 0 and biezace_zadanie is None


def petla_gry():
    global life, liczba_rund_od_poczatku, liczba_wykopanych__rud, liczba_wykopanych__kamieni, liczba__wykopanych__rubinow
    while czy_kontuowac_gre():
        opponent = wylosuj_przeciwnika()
        walcz_z_przeciwnikiem(opponent)
        odbierz_nagrode_za_pokonanie_przeciwnika(opponent)

# --------------przeciwnik-----------------------------------

def odbierz_nagrode_za_pokonanie_przeciwnika(opponent):
    global liczba_wykopanych__rud, liczba_wykopanych__kamieni, liczba__wykopanych__rubinow
    if (opponent[1] <= 0 and opponent[0] == ZASOB_RUDA):
        print('Wydobyłeś Rudę!!!')
        liczba_wykopanych__rud += 1
    elif (opponent[1] <= 0 and opponent[0] == ZASOB_KAMIEN):
        print('Wydobyłeś Kamień!!!')
        liczba_wykopanych__kamieni += 1
    elif (opponent[1] <= 0 and opponent[0] == ZASOB_RUBIN):
        print('Wydobyłeś Rubin!!!')
        liczba__wykopanych__rubinow += 1
    sprawdz_quest()



def walcz_z_przeciwnikiem(opponent):
    global life, liczba_rund_od_poczatku, liczba__wykopanych__rubinow, liczba_wykopanych__kamieni, liczba_wykopanych__rud, tryb_rozgrywki
    while opponent[1] > 0:
        print(f"{name} wydobywa teraz {opponent[0]}")
        if(tryb_rozgrywki != TRYB_BEZ_RUND):
            print(f"Aktualna runda {liczba_rund_od_poczatku} / {MAKSYMALNA_LICZBA_RUND}")
        print(
            f"{name} ma teraz {liczba_wykopanych__kamieni} {ZASOB_KAMIEN} , {liczba_wykopanych__rud} {ZASOB_RUDA}, {liczba_zlota} {ZASOB_ZLOTO}, {liczba__wykopanych__rubinow} {ZASOB_RUBIN}")
        print(f"Surowiec ma {opponent[1]} HP i zadaje Ci {opponent[2]} punkty wycięczenia")
        
        life -= opponent[2]
        if life <= 0:
            break
# ------------------------informacje----------------------------
        print(f"Masz {life} Punktów wycięczenia i {zasoby} dynamitu")
        atak = wybierz_sposob()
        opponent[1] -= atak
        if (biezace_zadanie != None):
            print("-" * 40)
            print(f"Uczestniczysz w zadaniu : {biezace_zadanie[1]}")
            if (sprawdz_quest()):
                break
            print("-" * 40)
        print(f"Zadałeś {atak} obrażeń")
        liczba_rund_od_poczatku += 1

# ----------------the-end--------------------------

def podsumowanie_gry():
    print("-" * 40)
    print("KONIEC GRY!")
    if (life <= 0):
        print("Umarłeś Z Wykończenia")
    elif (tryb_rozgrywki != TRYB_BEZ_RUND and liczba_rund_od_poczatku >= MAKSYMALNA_LICZBA_RUND):
        print("Nie udało się wykonać zadań w wyznaczonym czasie")
    else:
        print(f"Wygrałeś!! Pozostało Ci {life} HP i {zasoby} dynamit")
        print(f"Wykopałeś {liczba_wykopanych__rud} Rudy Żelaza!!!")
        print(f"Wykopałeś {liczba_wykopanych__kamieni} Kamieni!!!")
        print(f"Wykopałeś {liczba__wykopanych__rubinow} Rubinów!!!")
        print(f"Liczba wykonanych zadań {liczba_wykonanych__zadan} w {liczba_rund_od_poczatku} rund!!!")

wybierz_tryb_gry()
petla_gry()
podsumowanie_gry()