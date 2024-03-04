
from administracja import Administracja
from admin import Admin
from IT import IT
from klienci import Klienci
from deweloperzy import Deweloperzy
from HR import HR
from konsulaci import Konsultanci
from ksiegowosc import Ksiegowosc
from zarzad import Zarzad





def wybierz_sposob():
    print('a/A - Pokaz Administracje')
    print('b/B - Pokaz IT')
    print('c/C - Pokaz klientow')
    print('d/D - Pokaz konsulatow')
    co = input().upper()
    if co == 'A':
        return administracja()
    elif co == 'B':
        return it()
    elif co == 'C':
        return klientow()
    elif co == 'D':
        return konsulatow()
    else:
        print("Nie wybrano akcji")
        return 0

def administracja():

#            """"""administracja"""""""

    a1 = Administracja("Alex",23,"prowadzenim bior")
    print(a1.przedstaw_sie())

    a2 = Administracja("Konrad",26,"kontrola korespondencji")
    print(a2.przedstaw_sie())

    a3 = Administracja("Julek",23,"sporzadzaniem pism")
    print(a3.przedstaw_sie())



def it():

#              """"""""it"""""""""""

    i1 = IT("Alex",23,"ddada")
    print(i1.przedstaw_sie())

    i2 = IT("Alex",23,"ddada")
    print(i2.przedstaw_sie())

    i3 = IT("Alex",23,"ddada")
    print(i3.przedstaw_sie())


def klientow():
# klienci

    kl1 = Klienci("Alex",23,"ddada")
    print(kl1.przedstaw_sie())

    kl2 = Klienci("Alex",23,"ddada")
    print(kl2.przedstaw_sie())

    kl3 = Klienci("Alex",23,"ddada")
    print(kl3.przedstaw_sie())


def konsulatow():
    
# Konsultanci

    ko1 = Konsultanci("Alex",23,"ddada")
    print(ko1.przedstaw_sie())

    ko2 = Administracja("Alex",23,"ddada")
    print(ko2.przedstaw_sie())

    ko3 = Administracja("Alex",23,"ddada")
    print(ko3.przedstaw_sie())


# ---------------------------------------------

#            """"""administracja"""""""

a1 = Administracja("Alex",23,"prowadzenim bior")
print(a1.przedstaw_sie())

a2 = Administracja("Konrad",26,"kontrola korespondencji")
print(a2.przedstaw_sie())

a3 = Administracja("Julek",23,"sporzadzaniem pism")
print(a3.przedstaw_sie())



#           HR

h1 = HR("Alex",23,"robieniem zadan")
print(h1.przedstaw_sie())

h2 = HR("Alex",23,"zbierania informacji")
print(h2.przedstaw_sie())

h3 = HR("Alex",23,"czyms")
print(h3.przedstaw_sie())



#                       ksiegowosc


ks1 = Ksiegowosc("Alex",23,"ddada")
print(ks1.przedstaw_sie())

ks2 = Ksiegowosc("Alex",23,"ddada")
print(ks2.przedstaw_sie())

ks3 = Ksiegowosc("Alex",23,"ddada")
print(ks3.przedstaw_sie())






#                          zarzad

za1 = Zarzad("Alex",23,"ddada")
print(za1.przedstaw_sie())

za2 = Zarzad("Alex",23,"ddada")
print(za2.przedstaw_sie())

za3 = Zarzad("Alex",23,"ddada")
print(za3.przedstaw_sie())

# -----------------------------------------------------

#              """"""""it"""""""""""

i1 = IT("Alex",23,"ddada")
print(i1.przedstaw_sie())

i2 = IT("Alex",23,"ddada")
print(i2.przedstaw_sie())

i3 = IT("Alex",23,"ddada")
print(i3.przedstaw_sie())





# admin
ad1 = Admin("Alex",23,"ddada")
print(ad1.przedstaw_sie())

ad2 = Admin("Alex",23,"ddada")
print(ad2.przedstaw_sie())

ad3 = Admin("Alex",23,"ddada")
print(ad3.przedstaw_sie())



# deweloperzy

d1 = Deweloperzy("Alex",23,"ddada")
print(d1.przedstaw_sie())

d2 = Deweloperzy("Alex",23,"ddada")
print(d2.przedstaw_sie())

d3 = Deweloperzy("Alex",23,"ddada")
print(d3.przedstaw_sie())


# ---------------------------------------------------------

# klienci

kl1 = Klienci("Alex",23,"ddada")
print(kl1.przedstaw_sie())

kl2 = Klienci("Alex",23,"ddada")
print(kl2.przedstaw_sie())

kl3 = Klienci("Alex",23,"ddada")
print(kl3.przedstaw_sie())





# Konsultanci

ko1 = Konsultanci("Alex",23,"ddada")
print(ko1.przedstaw_sie())

ko2 = Administracja("Alex",23,"ddada")
print(ko2.przedstaw_sie())

ko3 = Administracja("Alex",23,"ddada")
print(ko3.przedstaw_sie())


