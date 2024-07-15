# 14 Toistorakenteen ohjaus, break ja continue -komennot
#
# Tehdään ohjelma, joka kertoo käyttäjän syötteen
# perusteella, että onko kyseessä karkausvuosi.
# 
# Karkausvuosi on kyseessä kun:
#
# - Vuosi on jaollinen neljällä...
# - paitsi sadalla jaollisina vuosina, jolloin vuoden
#   pitää olla jaollinen myös neljällä sadalla.
#
# Esimerkkejä karkausvuosista:
# - 1600
# - 1904
# - 1916  
# - 1932
# - 1936
# - 1940 
# - 1952   
# - 1992
# - 1996
# - 2000
# - 2004 
# - 2020


jatketaan = True

while jatketaan:

  print("Kirjoita 'ei', jos et halua jatkaa ohjelman käyttöä:")
  vastaus = input()
  if vastaus == "ei":
    jatketaan = False
    continue

  # Toistetaan karkausvuoden selvittävää ohjelman osaa.
  print("Anna jokin vuosiluku ja kerron onko kyseessä karkausvuosi.")
  vuosiluku = int(input())

  # Vuosi on jaollinen neljällä...
  if vuosiluku % 4 == 0:
    if vuosiluku % 100 == 0:
      if vuosiluku % 400 == 0:
        print("Kyseessä tosiaan on karkausvuosi.")
        print("Poistutaan While toistorakenteesta.")
        break
      else:
        print("Kyseessä ei ollutkaan karkausvuosi.")
    else:
      print("Kyseessä on karkausvuosi.")
  else:
    print("Kyseessä ei ole karkausvuosi.")



# Muuta ohjelman toimintaa
print("Ohjelman suoritus loppui.")
 
