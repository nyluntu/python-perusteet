# 13 Toistorakenne
#
# Toistorakenteella toistetaan lähdekoodiosiota 
# kunnes käyttäjän määrittelemä ehto toteutuu. 
#
# Toistorakenteiden avainsanoja ovat:
# 
# - while
# - for
#
# Tehdään ohjelma, joka tulostaa nykyisen kierroksen
# ja toistaa itseään annetun kierrosmäärän verran.

# While toistorakenne

kierros = 0
print("Anna tulostettavien kierrosten lukumäärä.")
kierroksia = int(input())

while kierros < kierroksia:
  print("Nykyinen kierros:", kierros)
  # kierros = kierros + 1
  kierros += 1

print("WHILE toistorakenne loppui")
print("")

# For toistorakenne

for kierros2 in range(kierroksia):
  print("Nykyinen kierros:", kierros2)

print("FOR toistorakenne loppui")

print("Tulostetaan luvut listan arvot")
luvut = [*range(8)]
print(luvut)