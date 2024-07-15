# 12 Selvitetään karkausvuosi
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

print("Anna jokin vuosiluku ja kerron onko kyseessä karkausvuosi.")
vuosiluku = int(input())

# Vuosi on jaollinen neljällä...
if vuosiluku % 4 == 0:
  if vuosiluku % 100 == 0:
    if vuosiluku % 400 == 0:
      print("Kyseessä tosiaan on karkausvuosi.")
    else:
      print("Kyseessä ei ollutkaan karkausvuosi.")
  else:
    print("Kyseessä on karkausvuosi.")
else:
  print("Kyseessä ei ole karkausvuosi.")