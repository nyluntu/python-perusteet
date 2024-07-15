# 07 Valintarakenne ja sisennysten käyttö
#
# Sisennykset ovat tärkeä osa Python ohjelmointikielen
# muotoilua ja voi alkuun aiheuttaa monia virhetilanteita.
#
# Valintarakenteella voidaan kertoa ohjelmalle, että mikä
# osa ohjelmasta suoritetaan. Tutustutaan If -valintarakenteeseen.

print("Anna jokin kokonaisluku väliltä 0-50:")
syote = input()

if int(syote) > 15:
  print("Luku on suurempi kuin 15.")
  print("Sisennetty rivi 1")
  print("Sisennetty rivi 2")

print("Ilman sisennystä")
print("Ohjelman suoritus on loppu")
