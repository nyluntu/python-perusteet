# 11 Etsitään syötteista suurin arvo
#
# Sovelletaan tähän asti opittua. Tehdään ohjelma
# joka kysyy kolme kokonaislukua ja tulostaa niistä
# suurimman arvon.

print("Kerro kolme kokonaislukua ja etsin niistä sinulel suurimman arvon.")
print("Anna ensimmäinen luku:")
arvo1 = int(input())

print("Anna toinen lukusi:")
arvo2 = int(input())

print("Anna viimeinen lukusi:")
arvo3 = int(input())

print("Etsin suurinta lukua...")

suurin_luku = None

if arvo1 >= arvo2 and arvo1 >= arvo3:
  suurin_luku = arvo1
elif arvo2 >= arvo1 and arvo2 >= arvo3:
  suurin_luku = arvo2
else:
  suurin_luku = arvo3

if suurin_luku == None:
  print("Suurinta lukua ei ole olemassa.")
else:
  print("Suurin luku annetuista on", suurin_luku)